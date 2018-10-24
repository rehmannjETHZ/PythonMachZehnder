import numpy as np 
import math
import matplotlib.pyplot as plt

 #measurement 1
angle_eraser_one = np.array([172, 157, 142, 127, 112, 97, 82])
mV_max_one = np.array([-140., -15., 32., 31., -12., -150., -330.])
mV_min_one = np.array([-372., -230., -135., -133., -242., -415., -620.])
mV_max_one_rescaled = -mV_min_one
mV_min_one_rescales = -mV_max_one

#bad data measurement 2
angle_eraser_two = np.array([180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125,	
						120, 115, 110, 105, 100, 95, 90])
mV_max_two = np.array([-280., -220., -174., -126., -94., -72., -53.,-50., -47., 
					-59.,  -54., -52., 50.,  -65., -78., -113., -146., -196., -246.])
mV_min_two = np.array([-606., -560., -500., -447., -397., -350., -309., -268., -233.,
					-205.,  -209., -233., -288., -326., -380.,-454., -520., -587., -639.])
mV_max_two_rescaled = -mV_min_two
mV_min_two_rescaled = -mV_max_two


#measurement 3 bad data
angle_Ptwo = np.array([45, 52, 59, 66, 73, 80, 87, 94, 101, 108, 115, 122, 129, 136]) #P2 polariser adjusted
mV_max_three = np.array([230., 233., 233., 215., 210., 194., 177., 173., 197., 234., 291., 351., 400., 407.]) #mV
mV_min_three = np.array([42., 44., 37., 35., 39., 35., 39., 41., 45., 68., 115., 175., 227., 243.])
noise_max_three = 82.
noise_min_three = -44.
mV_max_three_rescaled = -mV_min_three
mV_min_three_rescaled = -mV_max_three

#measurement 4
angle_eraser_four = np.array([0, 10, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100])
mV_max_four = np.array([-135., -205., -275., -326., -322., -330., -336., -330., -316., -305., -290.,-259., -196., -126., -55.])
mV_min_four = np.array([-386., -504., -628., -731., -740., -763., -772., -760., -742., -713., -686., -643., -540., -409., -286.])


x_one = np.linspace(82, 172, 50)
x_two = np.linspace(90, 180, 50)
x_three = np.linspace(45, 135, 50)
x_four = np.linspace(0, 180, 50)

def contrast(V_max, V_min):
	return (V_max - V_min)/(V_max + V_min)

print(contrast(mV_max_one, mV_min_one))
print(mV_min_one.shape, mV_max_one.shape)
plt.plot(angle_eraser_four, contrast(mV_max_four, mV_min_four), 'b+')
plt.plot(x_four, abs(np.cos(2*x_four /180 * math.pi - math.pi/4)), 'r')
plt.plot(angle_eraser_one, contrast(mV_max_one, mV_min_one), 'g+')
plt.plot(angle_eraser_two, contrast(mV_max_two, mV_min_two))
plt.xlabel('angle of the eraser [°]')
plt.ylabel('contrast [1]')
plt.show()

