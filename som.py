import loadData
from numpy import *
import random
from math import *
numOfCluster=16
movies=1682
def distance(vectorA,vectorB):
    return sum((vectorA-vectorB)**2)

def initializeClusters():
    randMovieRatings=[]
    clusters=mat(zeros((numOfCluster,movies)))
    # coordinates=mat(zeros((sqrt(numOfCluster),numOfCluster)))
    # coordinates=[]
    for i in range(numOfCluster):
        for j in range(movies):
            clusters[i,j]=int(random.randint(1,5))
    # for i in range(numOfCluster):
    #     coordinates.append(i)
    # print clusters
    return clusters

def som(dataSet):
    m=shape(dataSet)[0] # 943
    clusters=initializeClusters()# kXn n=1682
    minDistance=100000000
    minCluster=-1
    for i in range(m):
        for j in range(numOfCluster):
            distance=distance(clusters[j,:],dataSet[i,:])
            if distance<minDistance:
                minDistance=distance
                minCluster=j
        # print d
        # break
    # print m

def test():
    dataSet=loadData.loadTrainingData("u1.base")
    testSet,testLabel=loadData.loadTestData("u1.test")
    som(dataSet)
test()
