# Makefile for LaTeX project
MAIN=tfg_ivan

# List of LaTeX commands to run to build your document
LATEX=pdflatex
BIBTEX=bibtex
MAKEGLOSSARIES=makeglossaries
MAKEINDEX=makeindex

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(MAIN)
	$(MAKEGLOSSARIES) $(MAIN)
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot $(MAIN).fls $(MAIN).fdb_latexmk $(MAIN).glsdefs $(MAIN).ist $(MAIN).acn $(MAIN).acr $(MAIN).alg $(MAIN).glg $(MAIN).glo $(MAIN).gls $(MAIN).xdy $(MAIN).mw $(MAIN).pdf $(MAIN).loe $(MAIN).idx $(MAIN).loa $(MAIN).lol $(MAIN).ltb
