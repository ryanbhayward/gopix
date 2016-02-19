LATEX = latex
DVIPS = dvips -Ppdf -t letter
PPR = gopic

pdf: clean full good ps 
	ps2pdf $(PPR).ps

full:  
	$(LATEX) $(PPR)
	$(LATEX) $(PPR)
	$(LATEX) $(PPR)
	#bibtex $(PPR)
	#$(LATEX) $(PPR)
	#$(LATEX) $(PPR)
	#$(LATEX) $(PPR)

ps: $(PPR).dvi
	$(DVIPS) $(PPR) -o

good: $(PPR).dvi
	$(DVIPS) -Ppdf -G0 -tletter $(PPR) -o

clean:
	-@rm $(PPR).dvi $(PPR).aux $(PPR).log $(PPR).ps $(PPR).pdf

