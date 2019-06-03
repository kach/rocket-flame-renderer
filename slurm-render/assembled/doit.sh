#!/bin/bash
while true; do
	date;
	~/rocket-pbrt/rocket-pbrt/build/imgtool assemble --outfile tada.exr ../*.exr;
	~/rocket-pbrt/rocket-pbrt/build/imgtool convert tada.exr tada.png;
	mv tada.png ~/afs-home/WWW/tada.png;
	sleep 10;
done
