"""Draw the manuscript schematics directly as font-embedded vector PDFs.

Run: python figures/draw_schematics.py --output figures
Requires Python 3.9+ and Matplotlib. No TeX engine or network is used.
The diagrams express the defined model; they are not measurement plots.
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch

plt.rcParams.update({'font.family':'STIXGeneral', 'mathtext.fontset':'stix',
                     'font.size':9, 'pdf.fonttype':42, 'ps.fonttype':42,
                     'text.usetex':False, 'axes.unicode_minus':False})
CM = 1 / 2.54

class Drawing:
    def __init__(self, bounds):
        x0,y0,x1,y1 = bounds
        self.fig = plt.figure(figsize=((x1-x0)*CM,(y1-y0)*CM))
        self.ax = self.fig.add_axes([0,0,1,1], xlim=(x0,x1), ylim=(y0,y1))
        self.ax.set_aspect('equal'); self.ax.axis('off')
        self.nodes = {}
        self.labels = []

    def text(self,x,y,label,size=9,ha='center',va='center'):
        artist=self.ax.text(x,y,label,fontsize=size,ha=ha,va=va,
                            linespacing=1.15,clip_on=False,zorder=4)
        self.labels.append([artist,None])
        return artist

    def box(self,name,x,y,w,h,label,dashed=False,shape='rect',size=9):
        style = {'edgecolor':'black','facecolor':'white','linewidth':.55,
                 'linestyle':(0,(4,3)) if dashed else 'solid', 'zorder':2}
        if shape == 'diamond':
            obj = Polygon([(x-w/2,y),(x,y+h/2),(x+w/2,y),(x,y-h/2)],**style)
        elif shape == 'circle': obj = Circle((x,y),w/2,**style)
        else: obj = Rectangle((x-w/2,y-h/2),w,h,**style)
        self.ax.add_patch(obj); self.text(x,y,label,size)
        self.labels[-1][1]=(x-w/2,y-h/2,x+w/2,y+h/2)
        self.nodes[name] = (x,y,w,h,shape)

    def point(self,name,side):
        x,y,w,h,_ = self.nodes[name]
        return {'n':(x,y+h/2),'s':(x,y-h/2),'e':(x+w/2,y),
                'w':(x-w/2,y),'nw':(x-w/2,y+h/2),
                'ne':(x+w/2,y+h/2),'c':(x,y)}[side]

    def line(self,points,dashed=False):
        xs,ys=zip(*points)
        self.ax.plot(xs,ys,color='black',linewidth=.55,
                     linestyle=(0,(4,3)) if dashed else 'solid',zorder=1)

    def arrow(self,p,q,dashed=False,via=()):
        points=[p,*via,q]
        if via:self.line(points[:-1],dashed)
        self.ax.add_patch(FancyArrowPatch(points[-2],points[-1],
                         arrowstyle='-|>',mutation_scale=7.5,linewidth=.55,
                         color='black',shrinkA=0,shrinkB=0,
                         linestyle=(0,(4,3)) if dashed else 'solid',zorder=1))

    def edge(self,a,b,sa='s',sb='n',**kwargs):
        self.arrow(self.point(a,sa),self.point(b,sb),**kwargs)

    def frame(self,x,y,w,h):
        self.ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor='black',
                                   linewidth=.55,linestyle=(0,(4,3)),zorder=0))

    def save(self,out,name):
        # Fixed physical canvas: do not enlarge or rasterize the scientific figure.
        self.fig.canvas.draw()
        renderer=self.fig.canvas.get_renderer()
        x0,x1=self.ax.get_xlim();y0,y1=self.ax.get_ylim()
        for artist,node in self.labels:
            b=artist.get_window_extent(renderer).transformed(self.ax.transData.inverted())
            if b.x0<x0-.02 or b.x1>x1+.02 or b.y0<y0-.02 or b.y1>y1+.02:
                raise ValueError(name+': clipped label '+repr(artist.get_text()))
            if node and (b.x0<node[0]-.02 or b.x1>node[2]+.02 or b.y0<node[1]-.02 or b.y1>node[3]+.02):
                raise ValueError(name+': label exceeds node '+repr(artist.get_text()))
        self.fig.savefig(out/(name+'.pdf'),format='pdf',
                         metadata={'Creator':'Python Matplotlib','Producer':None,
                                   'CreationDate':None,'ModDate':None})
        plt.close(self.fig)

def draw(out):
    d=Drawing((-6.3,-6.12,6.3,2.0))
    for name,x,y,w,label in [('base',-3.8,0,3.2,'base state\n$\\sigma_0$'),
        ('trace',0,0,3.2,'recorded trace\nevents + observations'),
        ('policy',3.8,0,3.2,'label policy\n$x\\in\\mathbb{B}^{\\mathcal{A}}$'),
        ('selected',-3.8,-2.6,3.2,'selected state\n$\\sigma_x$'),
        ('project',0,-2.6,3.2,'project and replay\nin original order'),
        ('receipt',3.8,-2.6,3.2,'regenerated\nundo receipts'),
        ('check',0,-5.4,6.2,'independent checker\nreplay, observations, reverse')]:
        d.box(name,x,y,w,1.1,label)
    d.edge('base','trace','e','w');d.edge('trace','policy','e','w')
    d.edge('base','project','s','nw',via=[(-3.8,-1.35),(-1.6,-1.35)])
    d.edge('trace','project')
    d.edge('policy','project','s','ne',via=[(3.8,-1.35),(1.6,-1.35)])
    d.edge('project','selected','w','e');d.edge('project','receipt','e','w')
    d.edge('selected','check','s','nw',via=[(-3.8,-4.15),(-3.1,-4.15)])
    d.edge('receipt','check','s','ne',via=[(3.8,-4.15),(3.1,-4.15)])
    d.edge('trace','check','n','w',via=[(0,1.5),(-6,1.5),(-6,-5.4)])
    d.edge('policy','check','e','e',via=[(6,0),(6,-5.4)])
    d.save(out,'pipeline')

    d=Drawing((-3.7,-4.75,10.0,1.45))
    d.box('one',0,0,7.1,1,'at most one write per cell\nactive observation gives a signed implication')
    d.box('closure',0,-1.8,5.1,1,'least signed closure\nor a direct contradiction')
    d.box('two',7.25,0,5.1,1,'at most two writes per cell\na cell can realize $p\\vee q$')
    d.box('clause',7.25,-1.8,4.4,1,'retained reader gives\n$\\neg r\\vee p\\vee q$')
    d.box('np',7.25,-3.6,5.0,1,'choice + inhibition + policy\n3-SAT embedding')
    d.edge('one','closure');d.edge('two','clause');d.edge('clause','np')
    d.edge('one','two','n','n',via=[(0,.9),(7.25,.9)],dashed=True)
    d.text(3.7,1.14,'one additional write')
    d.save(out,'boundary')

    d=Drawing((-1.3,-4.25,10.85,.7))
    for name,x,label in [('base',0,r'$\sigma_0(c)=v_0$'),
        ('e1',3.2,r'$e_1$: $a$ writes $v_1$'),('e2',6.4,r'$e_2$: $b$ writes $v_2$'),
        ('e3',9.6,r'$e_3$: $d$ writes $v_3$')]:
        d.box(name,x,0,2.2,.8,label)
    for a,b in [('base','e1'),('e1','e2'),('e2','e3')]:d.edge(a,b,'e','w')
    for name,x,label in [('d1',3.2,r'$x_a$?'),('d2',6.4,r'$x_b$?'),('d3',9.6,r'$x_d$?')]:
        d.box(name,x,-2.0,1.1,.7,label,shape='diamond')
    for i,x in enumerate([0,3.2,6.4,9.6]):d.box('v'+str(i),x,-3.55,2.2,.8,'value $v_'+str(i)+'$')
    for i,x in [(1,3.2),(2,6.4),(3,9.6)]:
        d.edge('d'+str(i),'v'+str(i));d.text(x+.2,-2.78,'yes',ha='left')
    for a,b,x in [('d3','d2',8),('d2','d1',4.8)]:
        d.edge(a,b,'w','e');d.text(x,-1.76,'no')
    d.edge('d1','v0','w','n');d.text(1.3,-2.75,'no')
    d.save(out,'last-writer')

    d=Drawing((-2.2,-4.4,10.0,.9))
    for name,x,y,w,label in [('input',0,0,3.1,'serialized instance'),
        ('cert',4,0,3.2,'serialized certificate'),
        ('parser',0,-1.7,4.2,'strict independent parser'),
        ('sem',4,-1.7,3.3,'independent replay'),
        ('obs',8,-1.7,3.5,'observation evaluation'),
        ('rev',4,-3.5,4.3,'reverse regenerated receipts'),
        ('decision',8.2,-3.5,3.2,'accept / reject + reason')]:d.box(name,x,y,w,.9,label)
    d.edge('input','parser');d.edge('cert','parser','s','n')
    d.edge('parser','sem','e','w');d.edge('sem','obs','e','w')
    d.edge('sem','rev');d.edge('obs','decision');d.edge('rev','decision','e','w')
    d.save(out,'checker')

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent)
    output=parser.parse_args().output
    output.mkdir(parents=True,exist_ok=True)
    draw(output)
