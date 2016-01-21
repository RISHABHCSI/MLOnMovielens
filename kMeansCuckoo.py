import loadData
from numpy import *

def distance(a,b):# finding distance... vector implementation
	return sqrt(sum(power(a - b, 2)))

def initializeCentroid(dataSet,k):# initial value of centroids..
	n=shape(dataSet)[1]
	centroids=mat(zeros((k,n))) # kXn
	for j in range(0,n):
		mini=min(dataSet[:,j])
		maxi=max(dataSet[:,j])
		rangei=maxi-mini
		centroids[:,j] = mini + rangei * random.rand(k,1) # s.t. values donot exceed the maximum value of feature, can do random initialization of matrics between 1 and 5.. But this won't work for other data
    # print centroids
    return centroids

def kMeans(dataSet,k,totalUsers):
	m = shape(dataSet)[0]
	n=shape(dataSet)[1]
	clusterAssignment=[-1]*totalUsers #will contain which point is assigned to which cluster.. index will denote the user
	centroids = initializeCentroid(dataSet, k)
    # print centroids
    check=True
    while check:# while there's a change in cluster points
    	check=False
    	for i in range(0,m):
    		minDist=100000000000000
    		minDistanceCluster=-1
    		for j in range(0,k):
    			dist=distance(centroids[j,:],dataSet[i,:])
    			if dist<minDist:
    				minDist = dist
    				minDistanceCluster=j
    		if clusterAssignment[i] != minDistanceCluster: # if there's a change in assigned cluster
    			clusterChanged = True
    		clusterAssignment[i] = minDistanceCluster # update the cluster assigned
    	for i in range(0,k):
    		temp=[]# contain the list of users belong to a particular cluster(i)
    		for j in range(0,m):
    			if clusterAssignment[j]==i:
    				temp.append(j)
    		ptsInClust=mat(zeros((len(temp),n)))
    		for k in range(0,len(temp)):
    			ptsInClust[k,:]=dataSet[temp[k],:]
    		centroids[i,:] = mean(ptsInClust, axis=0) # update centroid
    return centroids, clusterAssignment

def test():
	dataSet=loadData.loadTrainingData("u.data")
	for x in range(20,40,2):
		centroids,clusterAssignment=kMeans(dataSet[:100,:],x,shape(dataSet)[0])# 15 clusters
        emptyPool=[]
        for i in range(100,shape(dataSet)[0]):
            emptyPool.append(i)
        print centroids
        return
        testFile="u"
        avg=0.0
        for i in range(1,6):
        	testData,testLabel=loadData.loadTestData(testFile+str(i)+".test")
        	m = shape(dataSet)[0]
        	totalError=0
        	index=0# for test Label no.
        	predictions=[]
        	for t in testData:
        		user,movie=int(t[0])-1,int(t[1])-1
        		label=testLabel[index]
        		clusterNum=clusterAssignment[user] # cluster number of the user to test
        		userInCluster=[]
        		for i in range(0,m):
        			if clusterAssignment[i]==clusterNum:
        				userInCluster.append(i)
        		sumOfRatings=0
        		count=0 # number of users who've watched the movie
        		for i in userInCluster:
        			if dataSet[i][movie]!=0:# if movie is watched
        				sumOfRatings+=dataSet[i][movie]
        				count+=1
        		if count==0:# if there is no user in the cluster who've watched the movie
        			ratingsPredicted=3
        		else:
        			ratingsPredicted=around(sumOfRatings/count)# average of the raings.. round-off
        		predictions.append(ratingsPredicted)
        		totalError+=absolute(ratingsPredicted-label)
        		index+=1
        	meanError=totalError/len(testData)
        	# print meanError
        	avg+=meanError
        print
        print float(avg)/5
# print meanError
	# standardDeviation=std(predictions)
	# print standardDeviation

test()
