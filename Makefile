LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = goboards

pdf: clean full good ps 
	ps2pdf $(PPR).ps

full: 
	$(LATEX) $(PPR)
	$(LATEX) $(PPR)
	$(LATEX) $(PPR)

ps: $(PPR).dvi
	$(DVIPS) $(PPR) -o

good: $(PPR).dvi
	$(DVIPS) -Ppdf -G0 -tletter $(PPR) -o

clean:
	-rm $(PPR).dvi $(PPR).blg $(PPR).bbl *.aux *.log $(PPR).ps $(PPR).pdf
