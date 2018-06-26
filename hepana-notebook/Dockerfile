FROM jupyter/scipy-notebook:latest

ARG ROOT_VERSION=v6-13-02
ARG USERNAME=jovyan

USER root
RUN apt-get update -yqq && \
apt-get install -yqq apt-utils
RUN apt-get install -yqq \
gnuplot \
git dpkg-dev cmake g++ gcc binutils \
texlive-font-utils texlive-binaries texlive-metapost \
ghostscript imagemagick
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${USERNAME}

RUN cd ~ && \
git clone http://github.com/root-project/root.git && \
cd root && git checkout -b ${ROOT_VERSION} ${ROOT_VERSION} && \
cd ~ && mkdir root-build && cd root-build && \
cmake -Dx11=OFF -Dastiff=OFF -Dbuiltin_afterimage=OFF -Dtmva=OFF -Droofit=OFF ../root && \
make && \
cd ~ && rm -r ~/root && mv ~/root-build ~/root

ENV PATH="$HOME/root/bin:$PATH" \
LD_LIBRARY_PATH="$HOME/root/lib:$LD_LIBRARY_PATH" \
PYTHONPATH="$HOME/root/lib:$PYTHONPATH" \
MANPATH="$HOME/root/man:$MANPATH" \
CMAKE_PREFIX_PATH="$HOME/root:$CMAKE_PREFIX_PATH" \
ROOTSYS="$HOME/root:$ROOTSYS"

RUN mkdir -p $HOME/scripts
COPY --chown=jovyan:users scripts/* ${HOME}/scripts/
ENV PATH="$HOME/scripts:$PATH" \
PYTHONPATH="$HOME/scripts:$PYTHONPATH" \
TEXINPUTS="$HOME/scripts:$TEXINPUTS"

WORKDIR ${HOME}/work/
