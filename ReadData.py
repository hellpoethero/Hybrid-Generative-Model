import datetime
import pandas as pd
import numpy as np
import random
from scipy import sparse
from scipy.special import digamma
from scipy.sparse import csr_matrix
from time import time


def read(path, dataset):
	trainFile = path + dataset + "train.csv"
	validationFile = path + dataset + "validation.csv"
	testFile = path + dataset + "test.csv"
	train = pd.read_csv(trainFile, header=None)
	validation = pd.read_csv(validationFile, header=None)
	test = pd.read_csv(testFile, header=None)

	train.columns = ["user_id", "loc_id", "count"]
	validation.columns = ["user_id", "loc_id", "count"]
	test.columns = ["user_id", "loc_id", "count"]

	train_df = function01(train, 1)
	validation_df = function01(validation, 1)

	train_df = pd.concat([train_df, validation_df])

	df = train_df
	df.columns = ['user_id', 'loc_id', 'train']
	df = df.sample(frac=1, random_state=123).sort_values(by=['user_id', 'train'], ascending=[1, 0])
	return df


def read_test(path, dataset):
	testFileRepeat = path + dataset + "test_repeated.csv"
	testFileNew= path + dataset + "test_new.csv"
	testRepeat = pd.read_csv(testFileRepeat, header=None)
	testNew = pd.read_csv(testFileNew, header=None)
	testRepeat.columns = ["user_id", "loc_id", "count"]
	testRepeat['repeated'] = 1
	testNew.columns = ["user_id", "loc_id", "count"]
	testNew['repeated'] = 0
	test_repeat_df = function01(testRepeat, 1)
	test_new_df = function01(testNew, 0)

	test_df = pd.concat([test_repeat_df, test_new_df])
	test_df.columns = ["user_id", "loc_id", "repeated"]
	test_df = test_df.sort_values(by=['user_id', 'loc_id'], ascending=[1, 1])
	test_df['count'] = 0
	# print(test_df)


	# trainFile = path + dataset + "train.csv"
	# validationFile = path + dataset + "validation.csv"
	# train = pd.read_csv(trainFile, header=None)
	# validation = pd.read_csv(validationFile, header=None)
	#
	# train.columns = ["user_id", "loc_id", "count"]
	# validation.columns = ["user_id", "loc_id", "count"]
	#
	# train_validation_df = pd.concat([train, validation])
	#
	# for r in zip(train_validation_df['user_id'], train_validation_df['loc_id'], train_validation_df['count']):
	# 	if prev_user == -1 or r[0] != prev_user:
	# 		# if r[0] != prev_user:
	# 		# 	test_history[prev_user] = history[history_index-1]
	# 		temp_his = csr_matrix((1, venueSize), dtype=int)
	# 		temp_count = 0
	# 		history[history_index] = csr_matrix(temp_his)
	# 	else:
	# 		if temp_count == 0:  # added for divide by zero
	# 			history[history_index] = temp_his
	# 		else:
	# 			history[history_index] = temp_his / temp_count
	# 	temp_his[(0, r[1])] += 1
	# 	temp_count += 1
	# 	prev_user = r[0]
	# 	history_index += 1

	# print(len(test_repeat_df))
	# print(len(test_new_df))
	# print(len(test_df))
	return test_df

def function01(data, train):
	array = []
	for index, row in data.iterrows():
		temp = [[row['user_id'], row['loc_id'], train]] * row['count']
		array.extend(temp)

	df = pd.DataFrame(array)
	# df = df.sample(frac=0.4, replace=True, random_state=1)
	df.columns = ["user_id", "loc_id", "train"]
	return df