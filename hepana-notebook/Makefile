.PHONY: all clean phd-notebook

all: phd-notebook lhcb-symbols-def.tex

clean:
	docker rmi phd-notebook
	rm lhcb-symbols-def.tex

lhcb-symbols-def.tex:
	wget https://raw.githubusercontent.com/avitase/phdscripts/master/lhcb-symbols-def.tex

phd-notebook: lhcb-symbols-def.tex
	docker build --rm -t hepana-notebook .
