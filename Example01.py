import ReadData
import Lda
import time
import os

path = "data/"
datasetName = "go_sf/"
# go_sf go_ny tw_ny tw_oc lastfm reddit_sample

folder_name = "results/" + datasetName[:-1]
# if !os.direxists(folder_name):
# os.makedirs(folder_name)
# print("created folder")

df = ReadData.read(path, datasetName)
df_test = ReadData.read_test(path, datasetName)

Ks = [4] # number of topic
iters = [100] # number of iteration
top_k = 100

Lda.init(df, df_test, Ks, iters, top_k, datasetName, "", folder_name)
