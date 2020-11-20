LATEX = latex
DVIPS = dvips -Ppdf -t letter
#PPR = digraph-negwt
PPR = net

pdf: clean full good ps 
	ps2pdf $(PPR).ps

full: 
	$(LATEX) $(PPR)

ps: $(PPR).dvi
	$(DVIPS) $(PPR) -o

good: $(PPR).dvi
	#$(DVIPS) -Ppdf -G0 -tletter $(PPR) -o
	$(DVIPS) -G0 $(PPR) -o

clean:
	-rm $(PPR).dvi $(PPR).blg $(PPR).bbl *.aux *.log $(PPR).ps $(PPR).pdf
