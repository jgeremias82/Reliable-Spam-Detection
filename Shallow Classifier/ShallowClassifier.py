import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
#import graphviz
from IPython import embed
import pickle
import os
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import precision_score, accuracy_score
from sklearn.externals import joblib
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

data = 'teste.csv'
arq_write = open('resultado.csv', 'w')
arq_write.write(data + '\n')
arq_write.write('Algoritmo;TN;FP;FN;TP;TNR;TPR\n')

#data = data.replace(":",",")
#dataset_gerar = data.split(',')
#dataset_gerar = dataset_gerar[0]
data_capture2 = data
print('')
print('')
print(data_capture2)
data_capture = pd.read_csv(data_capture2)
x = data_capture.drop('classe',axis=1)
y = data_capture['classe']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.30, random_state = 42)


############################################
###### DECISION TREE #######
############################################
# Making a decision tree with two levels.
clfTre = tree.DecisionTreeClassifier(max_depth=None)
clfTre.fit(xTrain, yTrain)
predictions = clfTre.predict(xTest)
## GERAR MATRIX DE CONFUSAO ##
cm_dt = confusion_matrix(yTest, predictions)
TN = cm_dt[0][0]
FP = cm_dt[0][1]
FN = cm_dt[1][0]
TP = cm_dt[1][1]
TNR = TN / (TN + FP)
TPR = TP / (TP + FN)
arq_write.write('DecisionTree;' + str(TN) + ';' + str(FP) + ';' + str(FN) + ';' + str(TP) + ';' + str(TNR) + ';' + str(TPR) + ';\n')
print("DECISION TREE OK ")