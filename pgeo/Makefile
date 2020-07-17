LATEX = latex
DVIPS = dvips -Ppdf -t unknown
PPR = geo

pdf: full good 
	ps2pdf $(PPR).ps

full:	
	$(LATEX) $(PPR)

good: $(PPR).dvi
	$(DVIPS) -D 1000 $(PPR) -o

clean:
	-@rm *.ps *.dvi *.blg *.bbl *.aux *.log $(PPR).toc $(PPR).ent

cleanup: clean
	-@rm $(PPR).pdf
