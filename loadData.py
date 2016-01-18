from numpy import *

def loadTrainingData(filename):
	fr=open(filename)
	lines=fr.readlines()
	returnMat=zeros((943,1682))
	for line in lines:
		lWords=line.split("\t")
		returnMat[int(lWords[0])-1,int(lWords[1])-1]=int(lWords[2])
	return returnMat

def loadTestData(filename):
	fr=open(filename)
	lines=fr.readlines()
	testData=zeros((len(lines),2))
	testLabel=[]
	i=0
	for line in lines:
		lWords=line.split("\t")
		testLabel.append(int(lWords[-2]))
		testData[i,:]=lWords[:2]
		i+=1
	return testData,testLabel

def loadItem(filename):
	fr=open(filename)
	lines=fr.readlines()
	returnMat=zeros((1682,19))
	i=0
	for line in lines:
		lWords=line.split("|")
		returnMat[i,:]=lWords[5:]
		i+=1
	return returnMat
