import numpy as np 
import matplotlib.pyplot as plt

angle_eraser = np.array([172, 157, 142, 127, 112, 97, 82])
mV_max = np.array([-140., -15., 32., 31., -12., -150., -330.])
mV_min = np.array([-372., -230., -135., -133., -242., -415., -620.])

def contrast(V_max, V_min):
	return (V_max - V_min)/(V_max + V_min)

plt.plot(angle_eraser, contrast(mV_max, mV_min), 'b+')
plt.show()