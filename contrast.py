import numpy as np 
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


 #measurement 1 bad data
angle_eraser_one = np.array([172, 157, 142, 127, 112, 97, 82])
mV_max_one = np.array([-140., -15., 32., 31., -12., -150., -330.])
mV_min_one = np.array([-372., -230., -135., -133., -242., -415., -620.])
mV_max_one_rescaled = -mV_min_one
mV_min_one_rescales = -mV_max_one

#bad data measurement 2 bad data
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


#measurement 5 - mean (measurement 26.10.2018) bad data
angle_eraser_five = np.array([0, 10, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])
mV_max_five = np.array([-59.03, -70.2, -82, -86.1, -89.4, -87.8, -86.3, -89.9, -77.35, -71.6, -67.32, -60.8, -40.4, -25.8,-12.09, -8.3, -2.3, 4.6, 2.9, -11, -21, -33.24, -44.5])
mV_min_five = np.array([-114, -147.7, -175.2, -193.6, -200, -202.8, -201.9, -198.1, -188.8, -179.8, - 170.3, -158, -126.9,-92.7,-58.35, -32.3, -14.6, -6.37, -9.47, -23.52, -44, -74.26, -104.5])
error = 5

#measurement 6 - mean (measurement 26.10.2018) bad data
angle_eraser_six = np.array([0, 25, 50, 75, 100])
mV_max_six = np.array([-37.5, -13, -8, -15, -27])
mV_min_six = np.array([-75.5, - 43, - 20, -30, -57])
error = 5

#measurement 7 - mean with averageing function (measurement 29.10.2018) bad data
angle_eraser_seven = np.array([0, 20, 40, 60, 80])
mV_max_seven = np.array([-17., -9., -3.5, -4.7, -9.7 ])
mV_min_seven = np.array([-34., -16.3, -5.4, -8.3, -25.6])

mV_max_five -= 5
mV_min_five -= 5


angle_eraser_eight = np.array([0, 10, 15, 20, 25, 30, 32, 34, 36, 38, 40, 45, 50, 55, 60, 70, 80, 90])
mV_max_eight = np.array([-35., -36.3, -38.4, -40., -46.,-50., -53., -57.6, -57.5, -56.8, -51., -49., -45., -46.1,-44., -46., -52.9, -67.])
mV_min_eight = np.array([-93., -86., -82.7, -74., -73.,-66.5, -66., -66.6, -67.2, -70.6,-68., -78.9, -86., -96.3,-103., -120., -135.1, -141.2])
angle_eraser_eight_error = 1 #value of one degree chosen
mV_error = 5 #chosen 

x_one = np.linspace(82, 172, 50)
x_two = np.linspace(90, 180, 50)
x_three = np.linspace(45, 135, 50)
x_four = np.linspace(0, 180, 50)
x_five = np.linspace(0, 100, 50)
x_six = np.linspace(0, 100, 200)

def contrast(V_max, V_min):
	return -(V_max - V_min)/(V_max + V_min)

def sin_fit(x, a, b, c, d):
	return a * abs(np.cos(b * x /180 + c)) + d

fit_points, __ = curve_fit(sin_fit, angle_eraser_eight, contrast(mV_max_eight, mV_min_eight))

xerr_eight = 1
yerr_eight = 5*np.sqrt(mV_max_eight**2 + mV_min_eight**2)/(mV_max_eight + mV_min_eight)**2
print(yerr_eight)
print(*fit_points)
plt.plot(angle_eraser_eight, contrast(mV_max_eight, mV_min_eight), 'b+')
plt.plot(x_six, sin_fit(x_six, *fit_points))
plt.plot(x_six, 0.4*abs(np.cos(1.2* 2*x_six /180 * math.pi + (math.pi-2.8)/4))+0.05, 'r')
plt.errorbar(angle_eraser_eight, contrast(mV_max_eight, mV_min_eight), yerr_eight, linestyle='')
plt.xlabel('angle of the eraser [deg]')
plt.ylabel('contrast [1]')
plt.legend(('data points', 'fit of $|\sin(2\cdot \phi)|$ for eye guidance', 'error bars of the data points'))
plt.savefig('eraser_angle.pdf')
plt.show()



