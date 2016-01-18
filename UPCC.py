import loadData
from numpy import *
	# print meanList
def correlation(dataSet,i):
	m=shape(dataSet)[0]
	n=shape(dataSet)[1]
	meanList=[]
	# for k in range(0,m):
	# 	count=0
	# 	rating=0
	# 	for j in range(0,n):
	# 		if dataSet[k,j]!=0:
	# 			count+=1
	# 			rating+=dataSet[k,j]
	# 	if count:
	# 		meanList.append(float(rating)/count)
	# 	else:
	# 		meanList.append(0.0)
	# print meanList
	# meanMatrix=mean(dataSet,axis=1)
	# print shape(meanMatrix)
	relation=mat(zeros((943,943)))
	for j in range(0,943):
		if j!=i:
			mean1=0.0
			mean2=0.0
			summation=0.0
			summation2=0.0
			summation3=0.0
			count=0
			for k in range(0,1682):
				if dataSet[i,k] and dataSet[j,k]:
					# print dataSet[i,k]
					# print dataSet[j,k]
					# print
					mean1+=dataSet[i,k]
					mean2+=dataSet[j,k]
					# summation+=((dataSet[i,k]-meanList[i])*dataSet[j,k]-meanList[j])
					# # print ((dataSet[i,k]-meanList[i])*dataSet[j,k]-meanList[j])
					# summation2+=(dataSet[i,k]-meanList[i])**2
					# summation3+=(dataSet[j,k]-meanList[j])**2
					count+=1
			if count:
				mean1/=count
				mean2/=count
			# print mean2
			# print mean1
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
				relation[i,j]=0
			else:
				# print summation
				# print summation2
				# print summation3
				# print
				relation[i,j]=float(summation)/((summation2*summation3)**(0.5))
			# print summation
			# print summation
			# break
	# print list(relation[])
	# print relation[i,:]
	return relation


def test():
	dataSet=loadData.loadTrainingData("u1.base")
	testSet,testLabel=loadData.loadTestData("u1.test")
	# print testSet
	# print shape(testSet)
	for i in range(shape(testSet)[0]-1,0,-1):
		relation=correlation(dataSet,int(testSet[i,0])-1)
		# relation=relation+1
		# print relation[i,:]
		summation=0.0
		answer=0.0
		count=0
		for j in range(0,shape(dataSet)[0]):
			if (int(testSet[i,0])-1)!=j:
				if dataSet[j,testSet[i,1]]:
					if relation[int(testSet[i,0])-1,j]>0:
						summation+=((dataSet[j,testSet[i,1]])*relation[int(testSet[i,0])-1,j])*5
					else:
						summation+=((dataSet[j,testSet[i,1]])*relation[int(testSet[i,0])-1,j])
					count+=1
		if count==0:
			answer=3
		else:
			answer=around(summation/(count))
		# break
		print answer
		# print summation
		# print count
		# print
		# break

	# print len(testSet)
	# for i in range(0,)
	# print dataSet
	# for i in range(0,)
	# print m,n
test()