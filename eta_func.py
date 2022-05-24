import numpy as np
from numpy import pi
import pylab as plt
from colorsys import hls_to_rgb

def colorize(z):
    r = np.abs(z)
    arg = np.angle(z) 

    # h = (arg + pi)  / (2 * pi) + 0.5
    #h = np.interp(r, (r.min(), r.max()), (0, 360))
    h = 1
    l = 1.0 - 1.0/(1.0 + r**0.3)    
    s = 0.8

    
    # real=np.real(z)
    # imagin=np.imag(z)

    # h = np.divide(imagin,np.imag(z.max()))* (2 * pi*10)
    # l = 0.5+0.5*np.divide(-real,np.real(z.max()))

    c = np.vectorize(hls_to_rgb) (h,l,s) # --> tuple
    c = np.array(c)  # -->  array of (3,n,m) shape, but need (n,m,3)
    c = c.swapaxes(0,2) 
    return c

N=1000
a = 13
minre = 0
maxre = 3
minim = -2*a
maxim = 2*a
# minre = -40
# maxre = 40
# minim = -40
# maxim = 40
x,y = np.ogrid[minre:maxre:N*1j, minim:maxim:N*1j]
z = x + 1j*y

moeblimit = 1.5
x2,y2 = np.ogrid[-moeblimit:moeblimit:N*1j, -moeblimit:moeblimit:N*1j]
z2 = x2 + 1j*y2
re = np.ones(10000)
im = np.linspace(-200, 200, 10000)



def eta(z,size):
    real = np.real(z)
    imaginar = np.imag(z)
    # summe = x + 1j*y
    summe = 0 
    for i in range(1,size):
        powpow = np.power(i,z)
        part = np.divide(1, powpow)*(-1)**i
        summe = np.sum([summe, part], axis=0)
        # if i%2:
        #     summe = summe+1/i**z
        # else:
        #     summe = summe-1/i**z

    return summe

def zeta(z,size):
    real = np.real(z)
    imaginar = np.imag(z)
    # summe = x + 1j*y
    summe = 0 
    for i in range(1,size):
        powpow = np.power(i,z)
        part = np.divide(1, powpow)
        summe = np.sum([summe, part], axis=0)
        # if i%2:
        #     summe = summe+1/i**z
        # else:
        #     summe = summe-1/i**z

    return summe

def fortsetz(z,size):
    real = np.real(z)
    imaginar = np.imag(z)
    # summe = x + 1j*y
    summe = 0 
    for i in range(1,size):
        powpow = np.power(i,z)
        part = np.divide(1, powpow)*(-1)**i
        summe = np.sum([summe, part], axis=0)
        # if i%2:
        #     summe = summe+1/i**z
        # else:
        #     summe = summe-1/i**z

    return summe

def moeb(w):
    return np.divide(2*w+1,-2*w+3)
    # return ((2*w+1)/(-2*w+3))
    

fig, subpl = plt.subplots(1,2)

w = eta(z,100)
img = colorize(w)
w2 = moeb(eta(z2,10))
img2 = colorize(w2)


for i in range(1):
    line = re+0.5+0.1*i-1+1j*im
    subpl[0].plot(np.real(line),np.imag(line))
    subpl[1].plot(np.real(moeb(line)),np.imag(moeb(line)))
pl1=subpl[0].imshow(img, extent=[minre,maxre,minim,maxim])
pl2=subpl[1].imshow(img2, extent=[-moeblimit,moeblimit,-moeblimit,moeblimit])

def init1():
    return pl1

def animate1(i):
    i=i*100
    if i>5: 
        w = zeta(z,i)
        # w = moeb(z)
        img = colorize(w)
        w2 = moeb(w)
        img2 = colorize(w2)
        pl1.set_array(img)
        pl2.set_array(img2)
    return pl1



# import matplotlib.animation as animation
# anim = animation.FuncAnimation(
#                                fig, 
#                                animate1, 
#                                init_func=init1,
#                                frames = 10,
#                                interval = 1000# / fps, # in ms                               
#                                )

# anim.save('zeta_moebeta.gif')
plt.show()