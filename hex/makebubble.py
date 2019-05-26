import numpy as np

f = open('bubble-test.pbrt', 'w')

f.write('''
Film "image"
  "string filename" "bubble.exr"
  "integer xresolution" 400
  "integer yresolution" 400

Sampler "halton" "integer pixelsamples" 64
Integrator "bdpt"

LookAt
  0 0 0
  0 1 1
  0 0 1

Camera "perspective" "float fov" 45

WorldBegin

Include "hex.pbrt"
LightSource "infinite" "string mapname" "../sky.exr" "spectrum scale" [2.0 2.0]
''')


def make_dome(R, num_samples):
    for i in range(num_samples):
        theta = np.random.random() * np.pi / 2 + np.pi / 4
        u = 1/2 + np.random.random() / 2
        r = np.random.random() * 10 + R
        x = np.cos(theta) * r * np.sqrt(1 - u**2)
        y = np.sin(theta) * r * np.sqrt(1 - u**2)
        z = r * u
        p = np.random.random() * 360
        q = np.random.random() * 360
        r = np.random.random() * 360
        f.write('''
    AttributeBegin
      Translate %f %f %f
      Scale 0.002 0.002 0.001
      Rotate %f 0 0 1
      Rotate %f 0 1 0
      Rotate %f 1 0 0
      ObjectInstance "hex"
    AttributeEnd
    ''' % (x, y, z, p, q, r))

make_dome(6.0, 2 ** 22)

f.write('WorldEnd')
f.close()
