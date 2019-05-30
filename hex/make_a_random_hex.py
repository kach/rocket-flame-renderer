import numpy as np

x = np.random.random() * 180
y = np.random.random() * 180
z = np.random.random() * 60
seed = np.random.randint(0xdeadbeef)

data = {
    'XROT': x,
    'YROT': y,
    'ZROT': z,
    'SEED': seed
}

with open('hex-template.pbrt') as f:
    template = f.read()

name = 'hex-{XROT}-{YROT}-{ZROT}-{SEED}.pbrt'.format(**data)

with open('tmp/' + name, 'w') as g:
    g.write(template.format(**data))

import os

os.system('cd tmp/; ../../../rocket-pbrt/build/pbrt %s' % name)
