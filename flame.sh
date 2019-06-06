#!/bin/bash
../3dfluid/fluid && pbrt flame.pbrt && imgtool convert flame.exr flame.png && feh flame.png
