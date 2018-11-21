import numpy as np
import matplotlib.pyplot as plt
import os #used for data path
from tqdm import tqdm



def mean(x):
    return sum(x)/np.size(x)

def weightedmean(x, w):
    return sum(x*w)/sum(w)

def var(x):
    return np.sqrt(mean(x*x) - mean(x)**2)

Time = []
Ramp = []
Digital = []
Bucketnumber = 40
Buckets = np.zeros((Bucketnumber))
allBuckets = np.zeros((Bucketnumber))
for i in range(6):
    Time =  np.genfromtxt('FringeReconstruct_%s.csv' % (i +1), delimiter=',')[3:-1, 0].tolist()
    Ramp = np.genfromtxt('FringeReconstruct_%s.csv' % (i +1), delimiter=',')[3:-1, 1].tolist()
    Digital = np.genfromtxt('FringeReconstruct_%s.csv' % (i +1), delimiter=',')[3:-1, 2].tolist()
    Size = len(Time)
    Ramp = [int(x*100) for x in Ramp]


    Threshhold = 4
    Leap = 10


    updown = []
    last = 0


    #generate an array where the lengths of up and down periods are listed
    #First determine an estimate for the length of a period

    changes = 0
    i = 0
    now = -1
    pbar = tqdm(total=Size)
    print(Size)

    while i < Size - 1:
        if last != now:
            updown = updown + [0]
        last = now
        if i >= Size - 5:
            break
        if (Ramp[i+1] > Ramp[i]) & (Ramp[i+5] > Ramp[i]):
            now = 1
        elif (Ramp[i+1] < Ramp[i]) & (Ramp[i+5] < Ramp[i]):
            now = -1
        else:
            now = last

        updown[-1] += 1
        pbar.update(1)
        i+=1
    pbar.close()

    #plt.plot(range(len(updown)), updown)
    #plt.show()


    #cut off incomplete start and ending

    Time = Time[updown[0]: int(len(Time)-updown[-1])]
    Digital = Digital[updown[0]: int(len(Time)-updown[-1])]

    updown = updown[1: -1]



    runs = np.size(updown)
    all = 0
    allCounts = np.zeros((runs, Bucketnumber))
    for j in tqdm(range(np.size(updown)-1)):
        Bucketsize = int(updown[j]/Bucketnumber) #Checkout Bucketsize in current periode.
        Rest = updown[j] - Bucketsize*Bucketnumber #size of leftover data in this periode
        k = 0

        if j%2 == 0:
            for l in range(Bucketnumber):
                k = 0
                while k < Bucketsize:
                    if Digital[all+l*Bucketsize+k] > Threshhold:
                        Buckets[l] += 1
                        k += Leap
                        allCounts[j, l] += 1
                    else:
                        k += 1
            k = 0
            while k < Rest:
                    if Digital[all+(l+1)*Bucketsize+k] > Threshhold:
                        Buckets[-1] += 1
                        k += Leap
                    else:
                        k += 1
            all += updown[j]
        else:
            all += updown[j]
            for l in range(Bucketnumber):
                k = 0
                while k < Bucketsize:
                    if Digital[all-(l*Bucketsize+k)] > Threshhold:
                        Buckets[l] += 1
                        k += Leap
                        allCounts[j, l] += 1
                    else:
                        k += 1
            k = 0
            while k < Rest:
                    if Digital[all - ((l+1)*Bucketsize-k)] > Threshhold:
                        Buckets[-1] += 1
                        k += Leap
                    else:
                        k += 1

    allBuckets = allBuckets + Buckets
dT = (Time[1] - Time[0])/(mean(updown)*Bucketnumber) #Time Passing for each bucket
print('dT', dT)

dCounts = [var(allCounts[:, i]) for i in range(np.size(allCounts[0, :])-1)]
print(type(Bucketnumber-1))

dCounts_sqrt = [np.sqrt(allBuckets[i]) for i in range(Bucketnumber-1)] #larger error

print(dCounts_sqrt)

dCounts = np.asarray(dCounts)
print(np.size(dCounts))
print(type(allBuckets), allBuckets.shape)


print(dCounts)
x = range(Bucketnumber-1)
print(np.size(x))
plt.errorbar(x, allBuckets[0:-1], yerr= dCounts_sqrt, fmt=' ')
plt.xlabel('Bucketnumber, each Bucket has an average length of sec')
plt.hist(range(Bucketnumber-1), Bucketnumber-1, weights=allBuckets[0:-1])
plt.show()
plt.savefig('fringe_reconstruction.pdf')





