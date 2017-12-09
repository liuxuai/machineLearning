
import operator
from os import listdir

import matplotlib
import matplotlib.pyplot as plt


from numpy import *

import re,os

# -------------------------------------------------
# import svmMLiA
# dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
#
# b, alphas = svmMLiA.smoSimple(dataArr,labelArr, 0.6, 0.001, 40)




# -------------------------------------------------

# import logRegres

# dataArr, lableMat = logRegres.loadDataSet()
# weights = logRegres.stocGradAscent1(array(dataArr),lableMat)
# logRegres.plotBestFit(weights)

# logRegres.multiTest()

# -------------------------------------------------
# import feedparser
#
# from bayes import *
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# vocabList,pSF,pNY = localWords(ny,sf)

# -------------------------------------------------
# from trees import *
# from treePlotter import *

# spamTest()

# regEx = re.compile(r'\W*')
# if os.path.exists('email/ham/6.txt'):
#     with open('email/ham/6.txt').read() as emailText:
#         listOfTokens = regEx.split(emailText)

# listoPosts, listClasses = loadDataSet()
# myVocabList = createVocabList(listoPosts)
# trainMatrix = []
# for postingDoc in listoPosts:
#     trainMatrix.append(setOfWords2Vec(myVocabList,postingDoc))
# p0V, p1V, pAb = trainNB0(traingMat,listClasses)

# testingNB()

# datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
# normMat,range,minVals = autoNorm(datingDataMat)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()
#
#
# datingClassTest()
#
# classifyPerson()

# handwritingClassTest()

# -------------------------------------------------
#from kNN import *
def createDataSet():
    # dataSet = [[1, 1, 'yes'],
    #            [1, 1, 'yes'],
    #            [1, 0, 'no'],
    #            [0, 1, 'no'],
    #            [0, 1, 'no']
    #
    dataSet = [[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3],
               [4, 4, 4],
               [5, 5, 5]
               ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


myDat, labels = createDataSet()
dataMatrix = mat(myDat)
dataMatrix*dataMatrix[2,:].T
#
# alfphas = mat(zeros(5,1))

# # calcShannonEnt(myDat)
# # chooseBestFeatureToSplit(myDat)
# # myTree = createTree(myDat,labels)
# # createPlot(myTree)
# myTree2 = retrieveTree(0)
#
# # classify(myTree2,labels,[1,0])
#
# fr = open('lenses.txt')
# lenses = [inst.strip().split('\t') for inst in fr.readline()]
# lensesLabels = ['age','prescript','astigmatic','tearRate']
# lensesTree = createTree(lenses,lensesLabels)

