.PHONY: all clean notebook

all: notebook 

clean:
	docker rmi phd-notebook

scripts/lhcb-symbols-def.tex: ../lhcb-symbols-def.tex
	cp ../lhcb-symbols-def.tex scripts/

notebook: scripts/lhcb-symbols-def.tex
	docker build --rm -t hepana-notebook:local .
