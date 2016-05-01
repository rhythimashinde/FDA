import numpy as np
import matplotlib.pyplot as plt
import csv
#import panda as pd
from scipy.interpolate import *
f=[]
a1=[]
a2=[]
a3=[]
samplesize=100
i=0
trainingsets = 10
while i<trainingsets:
        x=np.linspace(1,10,samplesize)
        #y=x**2
        y=5+x*np.cos(x)
        s=np.random.normal(y,1,samplesize)
        f.append(s)
        f.append(x)
        b = open('test1000final.csv', 'w')
        a = csv.writer(b)
        #print f
        a.writerows(f)
        p1=np.polyfit(x,s,1)
        p2=np.polyfit(x,s,2)
        p3=np.polyfit(x,s,3)
        plt.plot(x,s)
        plt.plot(x,np.polyval(p1,x),'r--')
        plt.plot(x,np.polyval(p2,x),'b--')
        plt.plot(x,np.polyval(p3,x),'m:')
        #print p1
        #print p2
        #print p3
        a1.append(p1)
        a.writerows(a1)
        a2.append(p2)
        a.writerows(a2)
        a3.append(p3)
        a.writerows(a3)
        i +=1
plt.show()
x=np.linspace(1,10,samplesize)

i=0
f0=[]

while i < 10:
    y=a1[i][0] * x + a1[i][1]
    f0.append(y)
    i = i + 1

##linear approximation f(x|T)
x=np.linspace(1,10,samplesize)

i=0
flinear=[]

while i < trainingsets:
    y=a1[i][0] * x + a1[i][1]
    flinear.append(y)
    i = i + 1

##the E[f(x|T)]
j = 0
expectedflinearlist = []

while j < samplesize:
    expectedflinear = sum(row[j] for row in flinear) / len(flinear)
    expectedflinearlist.append(expectedflinear)
    j = j + 1

##the f(x)
x=np.linspace(1,10,samplesize)
y=5+x*np.cos(x)

##the squared bias (f(x) - E[f(x|T)])^2
squaredbiaslist = list((np.array(y) - np.array(expectedflinearlist))**2)
squaredbiaslinear = reduce(lambda x, y: x + y, squaredbiaslist) / len(squaredbiaslist)
squaredbiaslinear

##the variance
variancelinear = []
i=0
while i < trainingsets:
    h=list((np.array(flinear[i]) - np.array(expectedflinearlist))**2)
    variancelinear.append(h)
    i = i + 1

expectedvariancelinearlist = []
j=0
while j < samplesize:
    expectedvariancelinear = sum(row[j] for row in variancelinear) / len(variancelinear)
    expectedvariancelinearlist.append(expectedvariancelinear)
    j = j + 1

finalvariancelinear = reduce(lambda x, y: x + y, expectedvariancelinearlist) / len(expectedvariancelinearlist)

print squaredbiaslinear
print finalvariancelinear

##quadratic approximation f(x|T)
x=np.linspace(1,10,samplesize)

i=0
fquadratic=[]

while i < trainingsets:
    y=a2[i][0] * (x)**2 + a2[i][1] * x + a2[i][2]
    fquadratic.append(y)
    i = i + 1

##the E[f(x|T)]
j = 0
expectedfquadraticlist = []

while j < samplesize:
    expectedfquadratic = sum(row[j] for row in fquadratic) / len(fquadratic)
    expectedfquadraticlist.append(expectedfquadratic)
    j = j + 1

##the f(x)
x=np.linspace(1,10,samplesize)
y=5+x*np.cos(x)

##the squared bias (f(x) - E[f(x|T)])^2
squaredbiaslist = list((np.array(y) - np.array(expectedfquadraticlist))**2)
squaredbiasquadratic = reduce(lambda x, y: x + y, squaredbiaslist) / len(squaredbiaslist)

##the variance
variancequadratic = []
i=0
while i < trainingsets:
    h=list((np.array(fquadratic[i]) - np.array(expectedfquadraticlist))**2)
    variancequadratic.append(h)
    i = i + 1

expectedvariancequadraticlist = []
j=0
while j < samplesize:
    expectedvariancequadratic = sum(row[j] for row in variancequadratic) / len(variancequadratic)
    expectedvariancequadraticlist.append(expectedvariancequadratic)
    j = j + 1

finalvariancequadratic = reduce(lambda x, y: x + y, expectedvariancequadraticlist) / len(expectedvariancequadraticlist)

print squaredbiasquadratic
print finalvariancequadratic

##cubic approximation f(x|T)
x=np.linspace(1,10,samplesize)

i=0
fcubic=[]

while i < trainingsets:
    y=a3[i][0] * (x)**3 + a3[i][1] * (x)**2 + a3[i][2] * x + a3[i][3]
    fcubic.append(y)
    i = i + 1

##the E[f(x|T)]
j = 0
expectedfcubiclist = []

while j < samplesize:
    expectedfcubic = sum(row[j] for row in fcubic) / len(fcubic)
    expectedfcubiclist.append(expectedfcubic)
    j = j + 1

##the f(x)
x=np.linspace(1,10,samplesize)
y=5+x*np.cos(x)

##the f(x|T)

##the squared bias (f(x) - E[f(x|T)])^2
squaredbiaslist = list((np.array(y) - np.array(expectedfcubiclist))**2)
squaredbiascubic = reduce(lambda x, y: x + y, squaredbiaslist) / len(squaredbiaslist)
squaredbiascubic

##the variance
variancecubic = []
i=0
while i < trainingsets:
    h=list((np.array(fcubic[i]) - np.array(expectedfcubiclist))**2)
    variancecubic.append(h)
    i = i + 1

expectedvariancecubiclist = []
j=0
while j < samplesize:
    expectedvariancecubic = sum(row[j] for row in variancecubic) / len(variancecubic)
    expectedvariancecubiclist.append(expectedvariancecubic)
    j = j + 1

finalvariancecubic = reduce(lambda x, y: x + y, expectedvariancecubiclist) / len(expectedvariancecubiclist)

print squaredbiascubic
print finalvariancecubic
