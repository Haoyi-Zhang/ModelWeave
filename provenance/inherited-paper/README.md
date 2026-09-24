# Paper source and assembly note

`main.pdf` is the current 50-page author-visible internal TOPLAS-style research draft. It uses the supplied, unmodified `acmart.cls` and `ACM-Reference-Format.bst` in `acmsmall,review,nonacm` mode.

The inherited 35-page manuscript was supplied only as a compiled PDF. Its substantive pages 1-33 are therefore included from `frozen-body.pdf`; the inherited two-page bibliography was replaced by the unified bibliography in this package. `frozen-body-text.txt` preserves extracted text for audit, but it is not represented as recovered LaTeX. The editable material in this delivery comprises `main.tex`, `appendix.tex`, `references.bib`, and the reconstructed TikZ sources under `figures/`. Those TikZ files restate only concepts already present in the inherited manuscript; they do not replace the missing source of pages 1-33.

Build from this directory:

```sh
make all
make check
```

The explicit BibTeX selection in the Makefile works around installations where the ordinary `bibtex` wrapper is unavailable or broken. A manual equivalent is:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex.original main   # use bibtex8 or bibtex where appropriate
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The paper target of exactly 50 pages is an internal planning contract, not a claimed publisher limit. The current PDF was rendered and inspected page by page. The missing editable source for pages 1-33 remains an external-upload readiness hold even though the assembled PDF is complete and reproducible from the files supplied here.
