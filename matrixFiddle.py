import numpy as np
from matplotlib import pyplot as plt

import random
primes = np.loadtxt(r'primes.txt',dtype ='int').flatten().tolist()
primes = primes[0:50]
size = max(primes)

pa = np.zeros([size,size])

for prime in primes:
	color = random.randint(1,1)
	pa[:,prime-1]+=color
	pa[prime-1,:]+=color
pa[pa<=1]=0

# im = plt.imshow(pa, interpolation="none", vmin = 0, vmax=2, cmap='spectral')
# plt.show()
# raw_input()


# size = 200
# mod = .5
# f = lambda x,y: abs((((x-y)/(y+x))%mod)-mod/2.0)
# a =  np.fromfunction(f, (size,size)).T
# plt.imshow(a, cmap='magma')
# plt.show()
# b= np.argsort(a.flatten())
# b = b.reshape((size, size))
# b = a > np.nanmax(a)-np.nanstd(a)*.3
# print b
# plt.imshow(b, interpolation="none", vmin = 0, vmax=1, cmap='bone')
# plt.show()

# raw_input()

import matplotlib.animation

W=200
W=size
T=18
basis = lambda x,y: ((x-y)/(y+x))
# basis = lambda x,y: x/y
a =  np.fromfunction(basis, (W,W))
c=a*0.0

fig = plt.figure()
im = plt.imshow(a, interpolation="spline16", vmin = 0, vmax=.5, cmap='bone')
title = plt.title("")
# plt.show()

def update(t):
	mod = float(T-t)/T/float(T)
	print(mod)
	b = np.abs(np.remainder(a, mod)/mod-mod/2.0)
	# b = np.roll(b, t)
	# b = np.roll(b, t,axis=0)
	global c
	c=(c+b)/2 +pa
	c = b
	# c=b+pa
	
	# c=np.rot90(c)
	# c=c.T
	# c=(c-b)/(b+c)
	im.set_array(c)
	# im.set_array(b)
	title.set_text(str(t))

def update2(t):
	mod = float(T-t)/T/float(T)
	b = np.abs(np.remainder(a, mod)-mod/2.0)
	r = np.argsort(b.flatten())
	r = r.reshape((W, W))
	r = b > np.nanmax(b)-np.nanstd(b)*mod*500
	
	global c
	c=r+pa
	c=r
	
	im.set_array(c)
	title.set_text(str(t))
	
ani = matplotlib.animation.FuncAnimation(fig, func=update2, frames=T, 
                       repeat=False, interval=1)
plt.show()