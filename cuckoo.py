import loadData
from numpy import *
import random


def initialization(dataSet,k):
    cluster=[]
    startIndex=0
    meanList=[]
    for i in range(k):
        cluster.append([])
        # sum=0.0
        for j in range(startIndex,startIndex+10):
            cluster[-1].append([j,dataSet[j,:]])
        meanList.append(mean(dataSet[startIndex:startIndex+9,:],axis=0))
        startIndex+=10
    emptyPool=[]
    for i in range(startIndex,shape(dataSet)[0]):
        emptyPool.append(i)

    return cluster,emptyPool,meanList

def test():
    dataSet=loadData.loadTrainingData("u.data")
    for clu in range(55,75,2):
        avg=0.0
        for te in range(1,6):
            testData,testLabel=loadData.loadTestData("u"+str(te)+".test")
            clusters,emptyPool,meanList=initialization(dataSet,clu)
            while len(emptyPool):
                randVar=random.randint(0,len(emptyPool)-1)
                user=emptyPool[randVar]
                randNes=random.randint(0,len(clusters)-1)
                mae=float(sum(abs(dataSet[user,:]-meanList[randNes])))/1682
                mini=100000000
                count=0
                threshold=int(0.3*len(clusters[randNes]))
                minPerson=-1
                for i in range(0,len(clusters[randNes])):
                    mae=float(sum(abs(dataSet[clusters[randNes][i][0],:]-meanList[randNes])))/1682
                    if mae<mini:
                        count+=1
                        mini=mae
                        minPerson=clusters[randNes][i][0]
                if count:
                    if count>=threshold:
                        for c in clusters[randNes]:
                            if c[0]==minPerson:
                                q=clusters[randNes].index(c)
                                for t in range(0,1682):
                                    add=(meanList[randNes][t]*len(meanList[randNes]))-dataSet[minPerson,t]
                                    add=add/(len(meanList[randNes])-1)
                                    meanList[randNes][t]=add
                                del(clusters[randNes][q])
                        emptyPool.append(minPerson)
                    clusters[randNes].append([user,dataSet[user,:]])
                    ind=emptyPool.index(user)
                    for t in range(0,1682):
                        add=(meanList[randNes][t]*len(meanList[randNes]))+dataSet[user,t]
                        add=add/(len(meanList[randNes])+1)
                        meanList[randNes][t]=add
                    del(emptyPool[ind])

                # var+=1
            summation=0
            for c in clusters:
                # print len(c)
                summation+=len(c)
            # print summation
            totalError=0
            predictions=[]
            m = shape(dataSet)[0]
            index=0
            for t in testData:
            	user,movie=int(t[0])-1,int(t[1])-1
                # print user,movie
            	label=testLabel[index]
                check=False
                for i in range(0,len(clusters)):
                    for j in range(0,len(clusters[i])):
                        if clusters[i][j][0]==user:
                            count =0
                            tum=0.0
                            for k in range(0,len(clusters[i])):
                                if dataSet[clusters[i][k][0],movie]!=0:
                                    count+=1
                                    tum+=dataSet[clusters[i][k][0],movie]
                            if count!=0:
                                tum=tum/count
                            check=True
                        if check:
                            break
                    if check:
                        break
            	predictions.append(tum)
            	totalError+=absolute(tum-label)
                index+=1
            meanError=totalError/len(testData)
            # print meanError
            avg+=meanError
        print float(avg)/5
            # print i
            # mae=float(sum(abs(dataSet[user,:]-meanList[randNes])))/1682
            # clusters[randNes][i]
        # break
test()
