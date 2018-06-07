FROM jupyter/scipy-notebook:latest

USER root
RUN apt-get update -yqq && \
apt-get install -yqq --no-install-recommends gnuplot

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jovyan
WORKDIR /home/jovyan/work/

RUN mkdir /home/jovyan/scripts
COPY gp2png.sh gptools.py /home/jovyan/scripts/
