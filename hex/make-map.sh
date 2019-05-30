../../rocket-pbrt/build/imgtool undirmap tmp/hex-*.exr
../../rocket-pbrt/build/imgtool convert --scale 0.005 undirmap.exr undirmap-scaled.exr
../../rocket-pbrt/build/pbrt test-skyscene.pbrt
