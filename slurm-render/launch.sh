#!/bin/sh

i=$1
j=$2
k=$3
l=$4

~/rocket-pbrt/build/pbrt --outfile "out.$i.$k.exr" --cropwindow $i $j $k $l ../main.pbrt
