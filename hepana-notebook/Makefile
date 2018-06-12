.PHONY: all clean notebook

all: notebook 

clean:
	docker rmi phd-notebook
	rm lhcb-symbols-def.tex

scripts/lhcb-symbols-def.tex:
	wget -P scripts/ https://raw.githubusercontent.com/avitase/phdscripts/master/lhcb-symbols-def.tex

notebook: scripts/lhcb-symbols-def.tex
	docker build --rm -t hepana-notebook .
