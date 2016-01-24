import loadData
from numpy import *
from sklearn import *
	# print meanList
def meanOfMoviesWatched(dataSet,i):
	mean1=0
	count1=0
	for k in range(0,1682):#for finding mean of ith user
		mean1+=dataSet[i,k]
	mean1/=1682
	return mean1

def pearson(dataSet,i=1):
	m=shape(dataSet)[0]
	n=shape(dataSet)[1]
	relation=mat(zeros((1,m)))
	mean1=meanOfMoviesWatched(dataSet,i)
	for j in range(m):
		summation=0.0
		summation2=0.0
		summation3=0.0
		if i!=j:
			mean2=meanOfMoviesWatched(dataSet,j)
			for k in range(0,1682):
				if dataSet[i,k] and dataSet[j,k]:
					# mean1+=dataSet[i,k]
					# mean2+=dataSet[j,k]
					summation+=((dataSet[i,k]-mean1)*(dataSet[j,k]-mean2))
					# print ((dataSet[i,k]-mean1))
					# print (dataSet[j,k]-mean2)
					# print mean1
					# print mean2
					# print
					summation2+=((dataSet[i,k]-mean1)**2)
					summation3+=((dataSet[j,k]-mean2)**2)
					# count+=1
			# break
			if summation2==0.0 or summation3==0.0:
				relation[0,j]=0
			else:
				# print summation
				# print summation2
				# print summation3
				# print
				relation[0,j]=float(summation)/(sqrt(summation2*summation3))
	# print relation
	return relation

def test():
	dataSet=loadData.loadTrainingData("u.data")
	avg=0.0
	standardDeviation=0.0
	for x in range(1,6):
		testSet,testLabel=loadData.loadTestData("u"+str(x)+".test")
		# for i in range(shape(testSet)[0]):
		testLabel=testLabel[:100]
		index=0
		totalError=0
		mTest=0
		predictions=[]
		for t in testSet:
			user,movie=int(t[0])-1,int(t[1])-1
			label=testLabel[index]
			relation=pearson(dataSet,user)
			summation=0.0
			answer=0.0
			count=0
			for j in range(0,shape(dataSet)[0]):
				if user!=j:
					if dataSet[j,movie]!=0:
						summation+=((dataSet[j,movie])*relation[0,j])
						count+=1
			if count==0:
				answer=3
			else:
				answer=around(summation/(count))
			# print answer
			predictions.append(answer)
			totalError+=absolute(answer-label)
			index+=1
			mTest+=1
			if mTest==100:
				break

			# stdDeviation=
		meanError=float(totalError)/mTest
		predictions=array(predictions)
		avg+=meanError
		standardDeviation+=std(predictions)
		print metrics.classification_report(testLabel,predictions)
		# print meanError
	print
	print "Mean Absolute Error: "+str(float(avg)/5)
	print
	print "Standard Deviation: "+str(float(standardDeviation/5))
	print
test()
