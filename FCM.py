import loadData
from numpy import *
from sklearn import *

def distance(a,b):# finding distance... vector implementation
	return sqrt(sum(power(a - b, 2)))

def randomInitialization(dataSet,k):# initial value of centroids..
	n=shape(dataSet)[1]
	centroids=mat(zeros((k,n))) # kXn
	for j in range(0,n):
		mini=min(dataSet[:,j])
		maxi=max(dataSet[:,j])
		rangei=maxi-mini
		centroids[:,j] = mini + rangei * random.rand(k,1) # s.t. values donot exceed the maximum value of feature, can do random initialization of matrics between 1 and 5.. But this won't work for other data
	return centroids

def fcm(dataSet,mFuzzy,c,numOfIteration):
	m = shape(dataSet)[0]
	n=shape(dataSet)[1]
	clusterAssignment=[]
	w=randomInitialization(dataSet, c)
	u=mat(zeros((m,c)))
	d=mat(zeros((m,c)))
	for t in range(0,numOfIteration):
		for i in range(0,m):
			for j in range(0,c):
				d[i,j]=distance(dataSet[i,:],w[j,:])
		for i in range(0,m):
			for j in range(0,c):
				if d[i,j]==0:
					u[i,j]=1
				else:
					ans=0
					for l in range(0,c):
						deno=d[i,l]
						if deno!=0:
							ans+=pow((d[i,j]/deno),2/(mFuzzy-1))
					if ans==0:
						u[i,j]=1
					else:
						u[i,j]=1.0/ans
			# print u[i,j]
		for j in range(0,c):
			for k in range(0,n):
				num=0
				deno=0
				for i in range(0,m):
					# print u[i,j],float(pow(u[i,j],m)),dataSet[i,k]
					num+=pow(u[i,j],mFuzzy)*dataSet[i,k]
					deno+=pow(u[i,j],mFuzzy)
					# print num,deno
				w[j,k]=num/deno
				# print w[j,k]
	for q in range(0,m):
		maxi=-1000000000
		maxCluster=-1
		for j in range(0,c):
			if u[i,j]>maxi:
				maxi=u[i,j]
				maxCluster=j
		clusterAssignment.append(maxCluster)
	return u,clusterAssignment

def test():
	dataSet=loadData.loadTrainingData("u.data")
	u,clusterAssignment=fcm(dataSet,2,8,2)
	# centroids,clusterAssignment=kMeans(dataSet,x)# 15 clusters
	print u
	# return
	testFile="u"
	avg=0.0
	for i in range(1,6):
		testData,testLabel=loadData.loadTestData(testFile+str(i)+".test")
		m = shape(dataSet)[0]
		totalError=0
		index=0# for test Label no.
		predictions=[]
		# clusterAssignedCode
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
			print ratingsPredicted
			totalError+=absolute(ratingsPredicted-label)
			index+=1
		meanError=totalError/len(testData)
		# avg+=meanError
		# print metrics.classification_report(testLabel,predictions)

		# meanError=totalError/len(testData)
		print meanError
		# avg+=meanError
		# print predictions
		# predictions=array(predictions)
		# predictions=predictions-mean(predictions)
		# print predictions
		# standardDeviation=std(predictions)
		# print standardDeviation

	# print
	# print float(avg)/5
	# print meanError
	# standardDeviation=std(predictions)
	# print standardDeviation

test()
