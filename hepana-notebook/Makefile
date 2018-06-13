.PHONY: all clean notebook

all: notebook 

clean:
	docker rmi phd-notebook
	rm scripts/lhcb-symbols-def.tex

scripts/lhcb-symbols-def.tex: ../lhcb-symbols-def.tex
	cp ../lhcb-symbols-def.tex scripts/
	chmod 0444 scripts/lhcb-symbols-def.tex

notebook: scripts/lhcb-symbols-def.tex
	docker build --rm -t hepana-notebook:local .
