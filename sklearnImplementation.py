from sklearn.cluster import KMeans
from numpy import *
import loadData
# dataSet=loadData.loadTrainingData("u1.base")
from sklearn.decomposition import PCA

def testKMeansForPca(data):
	dataSet=loadData.loadTrainingData("u1.base")
	# centroids,clusterAssignment=kMeans(dataSet,15)# 15 clusters
	testData,testLabel=loadData.loadTestData("u1.test")
	clf=KMeans(n_clusters=15)
	clf.fit(data)
	clusterAssignment=clf.predict(data)
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
	print meanError
	standardDeviation=std(predictions)
	print standardDeviation

def testKMeans():
	dataSet=loadData.loadTrainingData("u1.base")
	# centroids,clusterAssignment=kMeans(dataSet,15)# 15 clusters
	testData,testLabel=loadData.loadTestData("u1.test")
	clf=KMeans(n_clusters=15)
	clf.fit(dataSet)
	clusterAssignment=clf.predict(dataSet)
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
	print meanError
	standardDeviation=std(predictions)
	print standardDeviation

def testPCA():
	dataSet=loadData.loadTrainingData("u1.base")#mXn
	pca = PCA(n_components=100)
	# data=pca(dataSet,100)
	data=pca.fit_transform(dataSet)
	testKMeansForPca(data)

# testPCA()
testKMeans()