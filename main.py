import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial
import os #used for data path
from tqdm import tqdm

# #load CSV file Jonas
# path_jonas = open(os.path.expanduser("~/Git_Repos/.../RCD_data2csv.csv"))
# data_file = np.genfromtxt(path_jonas, delimiter=',')


Time = np.array([])
Digital = np.array([])
Analog = np.array([])
for i in range(9):
    Time = np.append(Time, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',', encoding='utf8')[3:-1, 0])
    # Digital = np.append(Digital, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',')[3:-1, 2] )
    Analog = np.append(Analog, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',', encoding='utf8')[3:-1, 1])
Size = np.size(Time)
Length = 1e-2 #length of a measuring intervall in seconds
Bucketsize = int(Size/((Time[-1] - Time[0])/Length))
Threshhold = 2
Leap = 10

BucketsTime = np.zeros((int(((Time[-1] - Time[0])/Length))))
BucketsAmount = np.zeros((100))

for j in tqdm(range(Size-Bucketsize)[::Bucketsize]):
    k = 0
    while k < Bucketsize:
        if Analog[j+k]> Threshhold:
            BucketsTime[int(j/Bucketsize)] +=1
            k += Leap
        else:
            k += 1
    if BucketsTime[int(j/Bucketsize)] < 100:
        BucketsAmount[int(BucketsTime[int(j/Bucketsize)])] += 1

entries, bin_edges, patches = plt.hist(range(15), 15, weights=BucketsAmount[0:15]/sum(BucketsAmount[0:15]))
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1])
plt.errorbar(bin_middles, BucketsAmount[0:15]/sum(BucketsAmount[0:15]), yerr=np.sqrt(BucketsAmount[0:15])/sum(BucketsAmount[0:15]), capsize=4, elinewidth=1, linestyle=' ')


# poisson function, parameter lamb is the fit parameter

def poisson(k, lamb):
    return (lamb**k/factorial(k)) * np.exp(-lamb)

# fit with curve_fit
parameters, cov_matrix = curve_fit(poisson, bin_middles, entries)
print('lambda = ', parameters.round(2))
print('Bucketsize = ', Bucketsize)

# plot poisson-deviation with fitted parameter
index = 1
x_plot = np.linspace(0, 14, 100)
plt.plot(x_plot, poisson(x_plot, *parameters), 'r-', lw=2)
plt.xlabel('counts')
plt.ylabel('probability density')
plt.legend(('Poissionian best fit with $\lambda = $%.2f' %parameters.round(2), 'bins with relative counts', 'error bars'), loc='best')
plt.savefig('counting_stats_%i.pdf' %index)
plt.show()

def mean(x):
    return sum(x)/np.size(x)

def weightedmean(x, w):
    return sum(x*w)/sum(w)

def var(x):
    return np.sqrt(mean(x*x) - mean(x)**2)

