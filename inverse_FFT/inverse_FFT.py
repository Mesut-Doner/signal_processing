# -*- coding: utf-8 -*-

import signals as s

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as ffp

x_min=0
x_max=12
n=100
x=np.linspace(x_min,x_max,n)

plt.subplots(figsize=(11,15))

# y1=s.sinusoidal_function1(x)
# plt.subplot(411)
# plt.plot(x,y1)
# plt.title('Sinyal 1')

# y2=s.sinusoidal_function2(x)
# plt.subplot(412)
# plt.plot(x,y2)
# plt.title('Sinyal 2')

y3=s.sinusoidal_function1(x)+s.sinusoidal_function2(x)
plt.subplot(311)
plt.plot(x,y3)
plt.title('Sinyal 1 + Sinyal 2')

fft=ffp.fft(y3)
plt.subplot(312)
plt.plot(fft)
plt.title('FFT')


inverse=ffp.ifft(fft)
plt.subplot(313)
plt.plot(inverse)
plt.title('Ters Furye(IFFT):')
