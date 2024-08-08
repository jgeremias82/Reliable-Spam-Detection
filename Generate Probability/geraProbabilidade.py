import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from IPython import embed
import pickle
import os
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import precision_score, accuracy_score
import joblib
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

load_model = 'loadModel/'
saida = 'predictions/'
caminho = 'dataset/'


datasets = ['02-dos_conhecido.csv','01-conhecido.csv', 'dos_similar.csv', 'ataque_novo.csv', 'sevico_novo.csv',
            'probe_similar.csv', 'conteudo_similar.csv','conteudo_novo.csv']

models = ['_randomForest','_gradientBoosting','_mlp','_adaBoosting','_bagging']

#############################
## INICIO DO CÓDIGO .CSV ##
#############################

for dataset in datasets:
    for model in models:
        data_capture = pd.read_csv(caminho + dataset)
        xTest = data_capture.drop('class',axis=1)
        yTest = data_capture['class']

        #### ESCREVER ARQUIVO ####
        dt_write = open(saida + str(dataset) + '_' + str(model) + '_pred.csv', 'w')
        dt_write.write('arquivo,classe,predicao,prob_norm,prob_atk,\n')

        ############################################
        ###### TESTE #######
        ############################################
        print(model + ': START')
        algoritmo = joblib.load(load_model + 'know-treinamento' + model + '.pkl')
        predictions = algoritmo.predict(xTest)
        probability = algoritmo.predict_proba(xTest)

        for i in range(len(yTest)):

            atk = probability[i][0]
            atk = '{:f}'.format(atk)

            norm = probability[i][1]
            norm = '{:f}'.format(norm)

            classe = yTest[i]
            if(classe == 'normal'):
                classe = '0'
            elif(classe == 'attack'):
                classe = '1'

            classePred = predictions[i]
            if(classePred == 'normal'):
                classePred = '0'
            elif(classePred == 'attack'):
                classePred = '1'


            dt_write.write(str(model)+','+str(classe)+','+str(classePred)+','+str(atk)+','+str(norm)+',\n')


        dt_write.close()
        print(model + ': END')
        print('')