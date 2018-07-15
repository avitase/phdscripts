FROM jupyter/scipy-notebook:03b897d05f16

ARG ROOT_VERSION=v6-14-00
ARG USERNAME=jovyan

USER root
RUN apt-get update -yqq && \
apt-get install -yqq apt-utils
RUN apt-get install -yqq \
gnuplot \
git dpkg-dev cmake ninja-build binutils \
texlive-font-utils texlive-binaries texlive-metapost \
ghostscript imagemagick
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${USERNAME}

RUN cd ~ && \
git clone --progress https://github.com/root-project/root.git && \
cd root && git checkout -b ${ROOT_VERSION} ${ROOT_VERSION} && \
cd ~ && mkdir root-build && cd root-build && \
cmake \
-Dalien=OFF \
-Dasimage=OFF \
-Dastiff=OFF \
-Dbonjour=OFF \
-Dbuiltin_afterimage=OFF \
-Dbuiltin_ftgl=OFF \
-Dbuiltin_glew=OFF \
-Dcastor=OFF \
-Dchirp=OFF \
-Dcache=OFF \
-Dfitsio=OFF \
-Dgfal=OFF \
-Dglit=OFF \
-Dgviz=OFF \
-Dkrb5=OFF \
-Dldap=OFF \
-Dmonalisa=OFF \
-Dmysql=OFF \
-Dodbc=OFF \
-Dopengl=OFF \
-Doracle=OFF \
-Dpgsql=OFF \
-Drfio=OFF \
-Dsapdb=OFF \
-Dshadowpw=OFF \
-Dsqlite=OFF \
-Dsrp=OFF \
-Dssl=OFF \
-Dtbb=OFF \
-Dtmva=OFF \
-Dxft=OFF \
-Dxml=OFF \
-Dxrootd=OFF \
-Dx11=OFF \
-G Ninja ../root && \
ninja && \
cd ~ && rm -r ~/root && mv ~/root-build ~/root

ENV PATH="$HOME/root/bin:$PATH" \
LD_LIBRARY_PATH="$HOME/root/lib:$LD_LIBRARY_PATH" \
PYTHONPATH="$HOME/root/lib:$PYTHONPATH" \
MANPATH="$HOME/root/man:$MANPATH" \
CMAKE_PREFIX_PATH="$HOME/root:$CMAKE_PREFIX_PATH" \
ROOTSYS="$HOME/root:$ROOTSYS"

RUN pip install --upgrade pip && pip install uncertainties iminuit

RUN mkdir -p $HOME/scripts
COPY --chown=jovyan:users scripts/* ${HOME}/scripts/
ENV PATH="$HOME/scripts:$PATH" \
PYTHONPATH="$HOME/scripts:$PYTHONPATH" \
TEXINPUTS="$HOME/scripts:$TEXINPUTS"

WORKDIR ${HOME}/work/
