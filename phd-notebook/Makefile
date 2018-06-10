.PHONY: all clean phd-notebook

all: phd-notebook 

clean:
	docker rmi phd-notebook

phd-notebook: Dockerfile gp2png.sh gptools.py parula.pal
	docker build --rm -t phd-notebook .
