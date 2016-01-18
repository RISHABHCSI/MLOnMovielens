import loadData
from numpy import *

def distance(a,b):
	return sqrt(sum(power(a - b, 2)))

def initializeCentroid(dataSet,k):
	n=shape(dataSet)[1] # n=200
	# print n

	centroids=mat(zeros((k,n)))
	# print shape(centroids)
	for j in range(0,n):
		mini=int(min(dataSet[:,j]))
		maxi=int(max(dataSet[:,j]))
		rangei=maxi-mini
		# print mini,maxi,rangei
		# print  random.rand(k,1)
		# print shape(mini + rangei * random.rand(k,1))
		centroids[:,j] = mini + rangei * random.rand(k,1)
	return centroids


def deleteThis(dataSet):
	mini=int(min(dataSet[:,0]))
	maxi=int(max(dataSet[:,0]))
	rangei=maxi-mini
	print mini,maxi,rangei

# test()
def kMeans(dataSet,k):# 943X200 k=10
	m = shape(dataSet)[0]# 943
	n=shape(dataSet)[1]# 200
	# print m,n
	clusterAssignment = mat(zeros((m,2)))# 943X2
	clusterAssignment-=1
	# print clusterAssignment
	centroids = initializeCentroid(dataSet, k) # 943X200, k=10
	# print centroids[:,:10]
	# print centroids[4,329]
	print centroids


	# check=True
	# while check:
	# 	check=False
	# 	for i in range(0,m):
	# 		minDist=100000000000000
	# 		minDistanceCluster=-1
	# 		for j in range(0,k):
	# 			dist=distance(centroids[j,:],dataSet[i,:])
	# 			# print dist
	# 			if dist<minDist:
	# 				minDist = dist
	# 				minDistanceCluster=j
	# 		if clusterAssignment[i,0] != minDistanceCluster: 
	# 			# print clusterAssignment[i,0]
	# 			clusterChanged = True
	# 		clusterAssignment[i,:] = minDistanceCluster,minDist**2
	# 	# print centroids 
	# 	for i in range(0,k):

	# 		# ptsInClust = dataSet[nonzero(clusterAssignment[:,0].A==i)[0]]
	# 		temp=[]
	# 		for j in range(0,m):
	# 			if clusterAssignment[j,0]==i:
	# 				temp.append(j)
	# 		ptsInClust=mat(zeros((len(temp),n)))
	# 		for k in range(0,len(temp)):
	# 			ptsInClust[k,:]=dataSet[temp[k],:]
	# 		centroids[i,:] = mean(ptsInClust, axis=0)
	# # print clusterAssignment[:,0]
	# return centroids, clusterAssignment

def testKMeans(dataSet):
	# dataSet=loadData.loadTrainingData("um.base")
	# dataSet=loadData.loadTrainingData("u1.base")
	kMeans(dataSet,10)
	

	# centroids,clusterAssignment=kMeans(dataSet,10)
	# print clusterAssignment[:100,:]
	# testData,testLabel=loadData.loadTestData("um.test")
	# print testData[:20,:]



	# testData,testLabel=loadData.loadTestData("u1.test")
	# # print testLabel[:20]
	# m = shape(dataSet)[0]
	# # print clusterAssignment[0,0]
	# # print m
	# # print dataSet
	# totalError=0
	# index=0
	# predictions=[]
	# for t in testData:
	# 	user,movie=int(t[0])-1,int(t[1])-1
	# 	label=testLabel[index]
	# 	# print user,movie,label
	# 	clusterNum=clusterAssignment[user,0]
	# 	# print clusterNum
	# 	userInCluster=[]
	# 	for i in range(0,m):
	# 		if clusterAssignment[i,0]==clusterNum:
	# 			userInCluster.append(i)
	# 	sumOfRatings=0
	# 	count=0
	# 	# print userInCluster
	# 	for i in userInCluster:
	# 		# print dataSet[i][movie]
	# 		if dataSet[i][movie]!=0:
	# 			sumOfRatings+=dataSet[i][movie]
	# 			count+=1
	# 	if count==0:
	# 		ratingsPredicted=3
	# 	else:
	# 		ratingsPredicted=around(sumOfRatings/count)
	# 	predictions.append(ratingsPredicted)
	# 	totalError+=absolute(ratingsPredicted-label)
	# 	index+=1
	# meanError=totalError/len(testData)
	# print meanError

def pca(dataSet,k):# taking k dimensions
	meanValues=mean(dataSet,axis=0)#1Xn
	dataSet=mat(dataSet)
	dataSet=dataSet-meanValues
	m=shape(dataSet)[0]
	n=shape(dataSet)[1]
	covMat=(1.0/943)*(dataSet.T)*dataSet # nXn
	u,s,v=linalg.svd(mat(covMat),full_matrices=True)
	uReduced=u[:,:k]#nXk
	z=dataSet*uReduced
	return z

def test():
	dataSet=loadData.loadTrainingData("u1.base")#mXn
	data=pca(dataSet,200)
	testKMeans(data)# mX200
	# print shape(data)
	# print data
	# deleteThis(data)
test()