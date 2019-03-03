import csv
import random
import math
import copy
from collections import defaultdict

import numpy as np
import pandas as pd
# ------------------------------------------------------
# TODO : main program
# ------------------------------------------------------
def readFile(csvfile):
    # read all the stored items in file
    reader = csv.reader(csvfile)
    dataset = []
    for row in reader:
        # skip if header
        if 'id' in row:
            continue
        # get input attribute 1 - 9
        inp = []
        for r in range(1,9):
            inp.append(str(row[r]))
        dataset.append(inp)
    return dataset

def readTestFile(csvfile):
    # read all the stored items in file
    reader = csv.reader(csvfile)
    dataset = []
    for row in reader:
        # skip if header
        if 'id' in row:
            continue
        # get input attribute 1 - 8
        inp = []
        for r in range(1,8):
            inp.append(str(row[r]))
        dataset.append(inp)
    return dataset

# TO separate dataset by class value
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def underBaseCount(dataset, separateSet):
    separateClass = separateByClass(dataset)
    return len(separateClass[separateSet])/len(dataset)

def baseCount(dataset, separatedSet, label):
    sum = 0
    for i in range(len(dataset)):
        for j in range(0,len(dataset[i])-1):
            if(dataset[i][j] == label and dataset[i][7] == separatedSet):
                sum = sum + 1
    return sum

def generalCount(dataset, separateSet, label):
    sum = underBaseCount(dataset,separateSet)
    return baseCount(dataset,separateSet,label)/sum

def result(dataset, separateSet, dataTest):
    sum = 1
    arr = []
    for i in range(len(dataTest)):
        for j in range(len(dataset[i])-1):
            sum = sum * generalCount(dataset,separateSet,dataTest[i][j])
        sum = sum * underBaseCount(dataset,separateSet)
        arr.append(sum)
        sum = 1
    return arr

def separateResult(arrHigh,arrLow):
    arrResult = []
    for i in range(len(arrHigh)):
        if arrHigh[i] > arrLow[i]:
            arrResult.append('>50K')
        else:
            arrResult.append('<=50K')
    return arrResult

def resultInCsv(result):
    with open('./TebakanTugas1ML.csv', 'w', newline='') as csvfile:
        fieldnames = ['result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(0, len(result)):
            writer.writerow({'result':result[x]})

def main():
    with open('TrainsetTugas1ML.csv', 'rt') as csvfile:
        print('1. Please wait ...')
        dataset = readFile(csvfile)
        with open('TestsetTugas1ML.csv', 'rt') as csvfile:
            dataTest = readTestFile(csvfile)
            arrHigh = result(dataset,">50K",dataTest)
            arrLow = result(dataset,"<=50K",dataTest)
            hasil = separateResult(arrHigh,arrLow)
            resultInCsv(hasil)
main()
