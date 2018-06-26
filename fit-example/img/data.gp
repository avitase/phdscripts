set terminal epslatex size 2.8, 2.1 monochrome standalone "" 9 header '\newcommand{\mevcc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c^2}} \newcommand{\mevc}{\ensuremath{\mathrm{Me\kern -0.1em V\!/}c}} \newcommand{\gevcc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c^2}} \newcommand{\gevc}{\ensuremath{\mathrm{Ge\kern -0.1em V\!/}c}} \newcommand{\MagUp}{\ensuremath{\mathrm{\textit{Mag\kern -0.05em Up}}}} \newcommand{\MagDown}{\ensuremath{\mathrm{\textit{MagDown}}}} \newcommand{\Lb}{\ensuremath{\Lambda_b^0}} \newcommand{\Lz}{\ensuremath{\Lambda}} \newcommand{\Dz}{\ensuremath{D^0}} \newcommand{\Ks}{\ensuremath{K_s}} \newcommand{\jpsi}{\ensuremath{J\mskip -3mu/\mskip -2mu\psi\mskip 2mu}}'
set output 'data.tex'
load '/home/jovyan/scripts/parula.pal'
set datafile separator ','

set macros
set loadpath '/home/jovyan/scripts'

load 'csvdata.cfg'
datafile = 'data.csv'
fitfile = 'f.csv'

set yrange [0:]

plot datafile u 2:5:1:3:4:6 with xyerrorbars lc black pt 7 ps 0.7 t 'Data',\
     fitfile with steps t 'Fit'