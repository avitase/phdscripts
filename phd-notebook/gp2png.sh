#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo Usage $0 [script.gp] [img.tex]
  exit 1
fi

if [ ! -f "$1" ]; then
  echo Error: File \'$1\' does not exists.
  exit 1
fi

gpfile=$1
fullfile=$2
filename=$(basename "$fullfile")
extension="${filename##*.}"
filename="${filename%.*}"

gnuplot $gpfile

lualatex -interaction=nonstopmode ${filename}.tex
if [ "$?" -ne 0 ]; then
  echo Failure
  exit 1
fi

convert -density 600 -background white -alpha remove -units PixelsPerInch ${filename}.pdf ${filename}.png

mkdir -p img
mv ${filename}.{gp,png} img/
rm ${filename}{.aux,.tex,-inc.eps,-inc-eps-converted-to.pdf,.log}
