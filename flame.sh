#!/bin/bash
python flame.py && pbrt flame.pbrt && imgtool convert flame.exr flame.png && feh flame.png
