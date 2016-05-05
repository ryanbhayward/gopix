LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = mazepic

$(PPR).pdf: $(PPR).ps
	ps2pdf $(PPR).ps

$(PPR).ps: $(PPR).dvi
	$(DVIPS) -G0 $(PPR) -o

$(PPR).dvi: $(PPR).tex mzpic.epsbody *.mzdg
	./makemzdg.sh
	$(LATEX) $(PPR)

clean:
	-@rm $(PPR).dvi $(PPR).aux $(PPR).log $(PPR).ps $(PPR).pdf
	-@./cleanmzdg.sh
