from numpy import *
import loadData
from math import *

numClusters=16
users=943
movies=1682
learningRate=0.05
total_iterations=4
temp_radius=0
initRadius=4
time_constant=0.99997

# def distance(vectorA,vectorB):
# 	return sum((vectorA-vectorB)**2)

def initClusters():
	clusters = mat(zeros((numClusters,movies)))
	for i in range(numClusters):
		for j in range(movies):
			clusters[i,j]=int(random.randint(1,5))

	# print clusters
	return clusters
# initClusters()

# def SOM(trainData):
def update_learning_rate(initRate,curr_iter,total_iterations):
	val=(-1)*(float)(curr_iter+1)/total_iterations
	newRate=initRate*(pow(2.732,val))
	return newRate

def update_influence(centers,bmu,cluster,radius):
	x_dist=(centers[bmu,0]-centers[cluster,0])*(centers[bmu,0]-centers[cluster,0])
	y_dist=(centers[bmu,1]-centers[cluster,1])*(centers[bmu,1]-centers[cluster,1])
	distance=(-1)*(x_dist+y_dist)
	den=2*(radius**2)
	value=distance/den
	newInfluence=pow(2.732, value)
	return newInfluence

def update_radius(initRadius,time_constant,currentIteration):
	value=(-1)*(currentIteration/time_constant)
	newRadius=initRadius*(pow(2.732,value))
	return newRadius

def test():
	no_grids=0
	trainData=loadData.loadTrainingData("u1.base")
	# testData,testLabels=loadData.loadTestData("u1.test")
	# SOM(trainData)
	m=shape(trainData)[0]
	# print testData
	# print testLabels
	# print m
	# centers=mat(zeros((numClusters,2))

	clusters=initClusters()
	print clusters
	centers=mat(zeros((numClusters,2)))
	bmu_of=[0 for m in range(0,users)]
	radius=4
	# print "In test"
	for i in range (0,radius):
		for j in range (0,radius):
			if no_grids<numClusters:
				centers[no_grids,0]=i
				centers[no_grids,1]=j
				# print centers[no_grids,0]
				# print centers[no_grids,1]
				# print
				no_grids+=1
			else:
				break

	iterations=0
	temp_difference=0
	difference=[0 for m in range(numClusters)]
	# print shape(clusters)
	# for c in range(0,movies):
	# 	if clusters[0,c]==5:
	# 		print "usahiuhsauifhduisahfuiashfiuhsauifhuishfuisah"
		# print clusters[0,c]
	# print clusters[0,0]

	while radius>=1:
		for i in range (0,users):
			print i

			for j in range (0,numClusters):
				temp_difference=0
				for k in range (0,movies):
					temp_difference+=(trainData[i,k]-clusters[j,k])*(trainData[i,k]-clusters[j,k])
				difference[j]=sqrt(temp_difference)

			min_difference=10000001
			for j in range (0,numClusters):
				if difference[j]<min_difference:
					min_difference=difference[j]
					bmu_of[i]=j

			currentLearningRate=update_learning_rate(learningRate, iterations, total_iterations)
			temp_rating=0
			for j in range(0,numClusters):
				distance=math.sqrt((centers[bmu_of[i],0]-centers[j,0])*(centers[bmu_of[i],0]-centers[j,0])+(centers[bmu_of[i],1]-centers[j,1])*(centers[bmu_of[i],1]-centers[j,1]))
				if distance<radius:
					newInfluence=update_influence(centers, bmu_of[i], j, radius)
					netChange=0
					for k in range (0,movies):
						# print "updating"
						# print j,k
						# print trainData[i,k]
						# print clusters[j,k]
						# print
						rating_difference=trainData[i,k]-clusters[j,k]
						netChange=(currentLearningRate*newInfluence*rating_difference)
						temp_rating=clusters[j,k]
						temp_rating+=netChange
						clusters[j,k]=temp_rating
						if clusters[j,k]>5:
							clusters[j,k]=5
						if clusters[j,k]<1:
							clusters[j,k]=1
						# break
					# break
				# break
			# break
		print radius
		iterations+=1
		# temp_radius=update_radius(initRadius, time_constant, iterations)
		# radius=temp_radius
		radius-=1


			# break
		# break



	error=0
	count=0

	fr=open("u1.test")
	lines=fr.readlines()
	# testMat=mat(zeros(943,1682))
	for line in lines:
		word = line.split("\t")
		u=int(word[0])-1
		m=int(word[1])-1
		r=int(word[2])
		# testMat[int(word[0])-1,int(word[1])-1]=int(word[2])
		error+=abs(r-clusters[bmu_of[u],m])
		count+=1
	print error/count

test()
# init()
