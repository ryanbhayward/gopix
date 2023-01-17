LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = show

pdf: clean full good ps 
	ps2pdf $(PPR).ps

full: 
	$(LATEX) $(PPR)

ps: $(PPR).dvi
	$(DVIPS) $(PPR) -o

good: $(PPR).dvi
	$(DVIPS) -G0 $(PPR) -o

clean:
	-rm $(PPR).dvi $(PPR).blg $(PPR).bbl *.aux *.log $(PPR).ps $(PPR).pdf
