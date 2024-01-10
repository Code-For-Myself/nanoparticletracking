import pandas as pd
import numpy as np

data1 = pd.read_csv("Gold_Shutter483_dur90-001-alltracks.csv")


particleID = 1


indizes = []
for i in range(0, len(data1["Particle ID"])):
    if (data1["Particle ID"][i] == int(particleID)):
        indizes.append(i)
data = data1.loc[ indizes , [" X1"," Y1"," X2"," Y2"] ]
def distSquared(x1,y1,x2,y2):
    ausgabe = (x2-x1)**2 + (y2-y1)**2
    return ausgabe



X1 = np.array(data[" X1"])
Y1 = np.array(data[" Y1"])
X2 = np.array(data[" X2"])
Y2 = np.array(data[" Y2"])

summe = 0
print(len(X1))
for i in range(0, len(X1)):
    summe = summe + distSquared(X1[i], Y1[i], X2[i], Y2[i])
summe = summe / len(X1) * (166 * 10 ** (-9)) ** 2
D = summe / (4 / 30)
print("Diffusionskoeffizient in [m^2/s]\t" + str(D))