LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = gopic

$(PPR).pdf: $(PPR).ps
	ps2pdf $(PPR).ps

$(PPR).ps: $(PPR).dvi
	$(DVIPS) -G0 $(PPR) -o

$(PPR).dvi: $(PPR).tex *.eps
	$(LATEX) $(PPR)

*.eps: *.gdg
	./makegdg.sh

*.gdg: 
	./makegdg.sh

clean:
	-@rm $(PPR).dvi $(PPR).aux $(PPR).log $(PPR).ps $(PPR).pdf
	-@./cleangdg.sh
