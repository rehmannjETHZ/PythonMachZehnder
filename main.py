import numpy as np
import matplotlib.pyplot as plt
import os #used for data path
from tqdm import tqdm

# #load CSV file Jonas
# path_jonas = open(os.path.expanduser("~/Git_Repos/EvaluationMICADAS/RCD_data2csv.csv"))
# data_file = np.genfromtxt(path_jonas, delimiter=',')
# #format data file to only have the relevant number; this should be a 28 by 7 matrix
# DF = np.delete(np.delete(data_file, 0,0), np.s_[:4] ,1)
# print(DF.shape)
# # format of DF: 14C counts | 12C (HE) muA | 13C (HE) nA | 13 CH nA (molecular current) |r-time | cyc | sample weight

# Joël's file reader - Jonas file reader does not work at my computer... but as long as main is
# in the same directory as RDC_data2csv.csv this version should work everywhere.
Time = np.array([])
Digital = np.array([])
Analog = np.array([])
for i in range(9):
    Time = np.append(Time, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',')[3:-1, 0])
    # Digital = np.append(Digital, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',')[3:-1, 2] )
    Analog = np.append(Analog, np.genfromtxt('Photon_stats_0%s.csv' % (i +1), delimiter=',')[3:-1, 1])
Size = np.size(Time)
Length = 400e-4
Bucketsize = int(Size/((Time[-1] - Time[0])/Length))
Threshhold = 2
Leap = 10

BucketsTime=np.zeros((int(((Time[-1] - Time[0])/Length))))
BucketsAmount=np.zeros((100))

for j in tqdm(range(Size-Bucketsize)[::Bucketsize]):
    k = 0
    while k < Bucketsize:
        if Analog[j+k]> Threshhold:
            BucketsTime[int(j/Bucketsize)] +=1
            k += Leap
        else:
            k += 1
    if BucketsTime[int(j/Bucketsize)]<100:
        BucketsAmount[int(BucketsTime[int(j/Bucketsize)])]+=1

plt.hist(range(15), 15, weights=BucketsAmount[0:15])
plt.show()



def mean(x):
    return sum(x)/np.size(x)

def weightedmean(x, w):
    return sum(x*w)/sum(w)

def var(x):
    return np.sqrt(mean(x*x) - mean(x)**2)

