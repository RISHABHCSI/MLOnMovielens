import loadData
from numpy import *
from sklearn import *
def distance(a,b):
	return sqrt(sum(power(a - b, 2)))

def initializeCentroid(dataSet,k):
	n=shape(dataSet)[1]
	centroids=mat(zeros((k,n)))
	for j in range(0,n):
		mini=int(min(dataSet[:,j]))
		maxi=int(max(dataSet[:,j]))
		rangei=maxi-mini
		centroids[:,j] = mini + rangei * random.rand(k,1)
	return centroids



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

def kMeans(dataSet,k):
	m = shape(dataSet)[0]
	n=shape(dataSet)[1]
	clusterAssignment=[-1]*m #will contain which point is assigned to which cluster.. index will denote the user
	centroids = initializeCentroid(dataSet, k)
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
				if clusterAssignment[j]==i:# since clusterAssignment is a matrix.. otherwise clusterAssignment[j] will work
					temp.append(j)
			ptsInClust=mat(zeros((len(temp),n)))
			for k in range(0,len(temp)):
				ptsInClust[k,:]=dataSet[temp[k],:]
			centroids[i,:] = mean(ptsInClust, axis=0) # update centroid
	return centroids, clusterAssignment


def testKMeans(dataSet):
	for x in range(50,61,2):
		centroids,clusterAssignment=kMeans(dataSet,x)
		dataSet=loadData.loadTrainingData("u.data")
		testFile="u"
		avg=0.0
		standardDeviationError=0
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
			# print "Mean Absolute Error: "+str(meanError)
			# print
			avg+=meanError
			# print "Precision And Recall: "
			# print metrics.classification_report(testLabel,predictions)
			# print
			predictions=array(predictions)
			standardDeviationError+=std(predictions)
			# print "Standard Deviation: "+str(standardDeviationError)
			# meanActual=mean(array(testLabel))
			# standardDeviationActual=std(array(testLabel))
			# tValue=(meanActual-meanError)/( sqrt( (((standardDeviationActual)**2)/len(testLabel)) + (((standardDeviationError)**2)/len(predictions))  )  )
			# print "tValue: "+str(tValue)
		# 	break
		# break
		# print
		print "Mean Absolute Error: "+str(float(avg)/5)
		print
		print "Standard Deviation: "+str(float(standardDeviationError/5))
		print
		break
			# print meanError
			# standardDeviation=std(predictions)
			# print standardDeviation

def test():
	dataSet=loadData.loadTrainingData("u.data")#mXn
	data=pca(dataSet,100)
	testKMeans(data)
test()
