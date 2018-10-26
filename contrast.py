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


#measurement 5 - mean (measurement 26.10.2018)
angle_eraser_five = np.array([0, 10, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
mV_max_five = np.array([-59.03, -70.2, -82, -86.1, -89.4, -87.8, -86.3, -89.9, -77.35, -71.6, -67.32, -60.8, -40.4, -25.8,-12.09, -8.3, -2.3, 4.6, 2.9, -11, -21, -33.24, -44.5])
mV_min_five = np.array([-114, -147.7, -175.2, -193.6, -200, -202.8, -201.9, -198.1, -188.8, -179.8, - 170.3, -158, -126.9,-92.7,-58.35, -32.3, -14.6, -6.37, -9.47, -23.52, -44, -74.26, -104.5])
error = 5

mV_max_five -= 5
mV_min_five -= 5

x_one = np.linspace(82, 172, 50)
x_two = np.linspace(90, 180, 50)
x_three = np.linspace(45, 135, 50)
x_four = np.linspace(0, 180, 50)
x_five = np.linspace(0, 100, 50)

def contrast(V_max, V_min):
	return (V_max - V_min)/(V_max + V_min)


print(contrast(mV_max_five, mV_min_five))
plt.plot(angle_eraser_five, contrast(mV_max_five, mV_min_five), 'b+')
plt.plot(x_five, abs(np.cos(2*x_five /180 * math.pi - math.pi/4)), 'r')
plt.xlabel('angle of the eraser [°]')
plt.ylabel('contrast [1]')
plt.show()



