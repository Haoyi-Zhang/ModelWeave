SHELL := /bin/sh
PDFLATEX ?= pdflatex
BIBTEX := $(shell if command -v bibtex.original >/dev/null 2>&1; then echo bibtex.original; elif command -v bibtex8 >/dev/null 2>&1; then echo bibtex8; else echo bibtex; fi)

.PHONY: all clean check
all: main.pdf

main.pdf: main.tex appendix.tex references.bib frozen-body.pdf acmart.cls ACM-Reference-Format.bst $(wildcard figures/*.tex)
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(BIBTEX) main
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex

check: main.pdf
	@test "$$(pdfinfo main.pdf | awk '/^Pages:/ {print $$2}')" = 50
	@! grep -Eq 'Overfull|Undefined|LaTeX Warning|Package .* Warning' main.log
	@echo 'paper check: 50 pages; no selected LaTeX warnings'

clean:
	rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.toc
