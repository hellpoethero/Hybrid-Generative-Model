import ReadData02
import Lda04
import time
import os

path = "D:/Download/data_new1/"
datasetName = "go_sf/"
# go_sf go_ny tw_ny tw_oc lastfm reddit_sample

folder_name = "D:/Research/Project/LDA/results/190802/" + datasetName[:-1]
# if !os.direxists(folder_name):
# os.makedirs(folder_name)
# print("created folder")

df = ReadData02.read(path, datasetName)
df_test = ReadData02.read_test(path, datasetName)

Ks = [4] # number of topic
iters = [100] # number of iteration
top_k = 100

# with open(folder_name + "/" + datasetName[:-1] + ".csv", "w") as outFile:
Lda04.init(df, df_test, Ks, iters, top_k, datasetName, "", folder_name)
# datasetName = "lastfm/"
# folder_name = "D:/Research/Project/LDA/results/" + datasetName[:-1] + "_" + str(time.time())
# os.makedirs(folder_name)
#
# with open(folder_name + "/" + datasetName[:-1] + ".csv", "w") as outFile:
# 	Lda01.init(df, [], [], top_k, datasetName, outFile, folder_name)
