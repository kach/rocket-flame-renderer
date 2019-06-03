import os

for a in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
	for b in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
		os.system('sbatch -c 8 launch.sh %f %f %f %f' % (a, a + 0.1, b, b + 0.1))
