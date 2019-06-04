#!/bin/bash
~/rocket-pbrt/build/imgtool assemble --outfile tada.exr ../*.exr;
~/rocket-pbrt/build/imgtool convert tada.exr tada.png;
mv tada.png ~/afs-home/WWW/tada.png;
