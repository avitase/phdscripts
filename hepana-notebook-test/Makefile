.PHONY: all clean

all: notebook.sh

clean:
	rm notebook.sh

notebook.sh: 
	wget https://raw.githubusercontent.com/avitase/phdscripts/master/hepana-notebook/hepana-notebook.sh
	mv hepana-notebook.sh notebook.sh
	chmod u+x notebook.sh
