.PHONY: all clean notebook

all: notebook lhcb-symbols-def.tex

clean:
	docker rmi phd-notebook
	rm lhcb-symbols-def.tex

lhcb-symbols-def.tex:
	wget https://raw.githubusercontent.com/avitase/phdscripts/master/lhcb-symbols-def.tex

notebook: lhcb-symbols-def.tex
	docker build --rm -t avitase/hepana-notebook:latest .
