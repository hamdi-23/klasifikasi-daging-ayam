import csv
from numpy.core.fromnumeric import resize
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn import svm
import math
import pandas as pd 
import numpy as np 
import cv2 
import sys
import os

def training() :
    df = pd.read_csv("data_ayam.csv")
    X = df.drop(['file','class'], axis=1)
    Y = df.drop(['file','meanB','meanG', 'meanR','standar_devB','standar_devG','standar_devR','skewness_B','skewness_G','skewness_R'], axis=1)
    X_train, X_test, Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    Y_train = Y_train.values.ravel()
    clf = svm.SVC(kernel='linear', degree=3, gamma='auto', C=1.0)
    clf.fit(X_train,Y_train)
    Y_pred = clf.predict(X_test)

    akurasi = accuracy_score(Y_test,Y_pred)
    conf = confusion_matrix(Y_test,Y_pred)
    print("=====================")
    print("akurasi", akurasi)
    print("======================")


def prediksi() :
    
    df = pd.read_csv("data_ayam.csv")
    x = df.drop(['file','class'],axis=1)
    y = df.drop(['file','mean_B','mean_G','mean_R','stdev_B','stdev_G','stdev_R'],axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=42)
    Y_train = Y_train.values.ravel()
    clf = svm.SVC(kernel='linear', degree=3, gamma='auto', C=1.0)
    clf.fit(X_train,Y_train)
    path = r"D:/ujicoba/dataset/"
    image = cv2.imread(path)

    if os.path.isfile(r'D:\ujicoba\dataset'):
        resized_image = cv2.resize(image,(256,256))
        bgr = cv2.cvtColor(resized_image,cv2.COLOR_RGB2BGR)
        B = bgr[:,:,0]
        G = bgr[:,:,1]
        R = bgr[:,:,2]   

#menghitung jumlah pixel
        totalB = B.size
        totalG = G.size
        totalR = R.size

#menghitung jumlah nilai pixel

        jumlahB = B.sum()
        jumlahG = G.sum()
        jumlahR = R.sum()

        #mean(rata-rata)

        meanB = jumlahB/totalB
        meanG = jumlahG/totalG
        meanR = jumlahR/totalR

        #stdev

        stdB = ((B-meanB)**2).sum()
        stdG = ((G-meanG)**2).sum()
        stdR = ((R-meanR)**2).sum()
        hasilakhir_stdB = math.sqrt((stdB/totalB))
        hasilakhir_stdG = math.sqrt((stdG/totalG))
        hasilakhir_stdR = math.sqrt((stdR/totalR))

        #skewness

        meanijB = (B - meanB)
        meanijG = (G - meanG)
        meanijR = (R - meanR)

        skewnessB = (meanijB**3).sum()
        skewnessG = (meanijG**3).sum()
        skewnessR = (meanijR**3).sum()

        if skewnessB >= 0 :
            hasilakhir_skewB = math.pow(skewnessB/totalB, float(1)/3)
        elif skewnessB < 0 :
            hasilakhir_skewB = -np.float_power(abs(skewnessB/totalB), float(1)/3)
        if skewnessG >= 0 :
            hasilakhir_skewG = math.pow(skewnessG/totalG, float(1)/3)
        elif skewnessG < 0 :
            hasilakhir_skewG = -math.pow(abs(skewnessG/totalG), float(1)/3)
        if skewnessR >= 0 :
            hasilakhir_skewR = math.pow(skewnessR/totalR, float(1)/3)
        elif skewnessR < 0 :
            hasilakhir_skewR = -math.pow(abs(skewnessR/totalR), float(1)/3)

        fitur = [
            meanB,
            meanG,
            meanR,
            hasilakhir_stdB,
            hasilakhir_stdG,
            hasilakhir_stdR,
            hasilakhir_skewB,
             hasilakhir_skewG,
            hasilakhir_skewR
        ]
        citra = [[
            fitur[0],
            fitur[1],
            fitur[2],
            fitur[3],
            fitur[4],
            fitur[5],
            fitur[6],
            fitur[7],
            fitur[8]
        ]]
        Y_pred = clf.predict(citra)
        print("=========hasil=========")
        
        if Y_pred == 1 :
                print("===================================")
                print("dagng ayam masih segar")
                print("===================================")
        elif Y_pred == 2 :
            print("===================================")
            print("dagng ayam tidak segar")
            print("===================================")
        else :
            print("tidak diketahui")
    else :
        print("======================")
        print("citra tidak ditemukan")
        print("======================")
        sys.exit()
def evaluasi() :
    df = pd.read_csv("data_ayam.csv")
    x = df.drop(['file','class'],axis=1)
    y = df.drop(['file','mean_B','mean_G','mean_R','stdev_B','stdev_G','stdev_R'],axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=42)
    Y_train = Y_train.values.ravel()
    clf = svm.SVC(kernel='linear', degree=3, gamma='auto', C=1.0)
    clf.fit(X_train,Y_train)
    Y_pred = clf.predict(X_test)
   
    print(classification_report(Y_test, Y_pred))
    

