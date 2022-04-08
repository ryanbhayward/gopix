LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = show

$(PPR).pdf: $(PPR).ps
	ps2pdf $(PPR).ps

$(PPR).ps: $(PPR).dvi
	$(DVIPS) -G0 $(PPR) -o

$(PPR).dvi: $(PPR).tex body.eps *.cdg
	./makecdg.sh
	$(LATEX) $(PPR)

clean:
	-@rm $(PPR).dvi $(PPR).aux $(PPR).log $(PPR).ps $(PPR).pdf
	-@./cleancdg.sh
