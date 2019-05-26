import math

N = 6
R = 1
h = 1 # total height is 2h, of course

H1 = [ (math.cos(math.pi * 2 * t / N), math.sin(math.pi * 2 * t / N), +h) for t in range(N) ]
H2 = [ (math.cos(math.pi * 2 * t / N), math.sin(math.pi * 2 * t / N), -h) for t in range(N) ]

with open('hex.pbrt', 'w') as f:
    f.write('ObjectBegin "hex"\n')
    f.write('  AttributeBegin\n')
    f.write('  Material "glass" "float eta" 1.31 "spectrum Kr" [0.0 0.0]\n')
    f.write('  Shape "trianglemesh"\n')

    f.write('  "point P" [\n')
    f.write('    0 0 %d\n' % +h)
    f.write('    0 0 %d\n' % -h)
    for x, y, z in H1 + H2:
        f.write('    %f %f %f\n' % (x, y, z))
    f.write('  ]\n')

    f.write('  "integer indices" [\n')
    for i in range(N):
        a = (i % N) + 2
        b = ((i + 1) % N) + 2
        f.write('    %d %d %d\n' % (b, a, 0))
        f.write('    %d %d %d\n' % (a + N, b + N, 1))
        f.write('    %d %d %d\n' % (a, a + N, b + N))
        f.write('    %d %d %d\n' % (b + N, b, a))
    f.write('  ]\n')
    f.write('  AttributeEnd\n')
    f.write('''ObjectEnd\n''')
