import cv2
import numpy as np
import math
import os
import csv

def color_moment() :
    path = r"D:/ujicoba/dataset/"
    image_fitur = []
    for file in os.listdir(path):
        image=cv2.imread(os.path.abspath(path +"/"+file))
        print(file)
        resized_image= cv2.resize(image,(256,256))
        bgr = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)

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

#untuk labeling
        kelas = 0
        if file.startswith("segar") :
            kelas = 1
        else :
            kelas = 2

        fitur = {

            "file" : file,
            "meanB" : meanB,
            "meanG" : meanG,
            "meanR" : meanR,
            "standar_devB" : hasilakhir_stdB,
            "standar_devG" : hasilakhir_stdG,
            "standar_devR" : hasilakhir_stdR,
            "skewness_B" : hasilakhir_skewB,
            "skewness_G" : hasilakhir_skewG,
            "skewness_R" : hasilakhir_skewR,
            "class" : kelas
        }

        image_fitur.append(fitur)
        csv_columns = ['file','meanB','meanG', 'meanR','standar_devB','standar_devG','standar_devR','skewness_B','skewness_G','skewness_R','class']

        csv_file = "data_ayam.csv"
        try :
            with open(csv_file, 'w', newline='') as csvfile :
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data  in image_fitur :
                    writer.writerow(data)
        except IOError:
            print("I/O error")