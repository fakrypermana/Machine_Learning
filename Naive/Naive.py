import csv
import random
import math
import copy
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

# TO split into learn and train
def splitDataset(dataset, splitRatio):
    learnSize = int(len(dataset) * splitRatio)
    learns = []
    trains = list(dataset)
    while len(learns) < learnSize:
        index = random.randrange(len(trains))
        learns.append(trains.pop(index))
    return [learns, trains]

# TO separate dataset by class value
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        print('vector & separated',vector[1],'---',separated)
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def main():
    # open file
    splitRatio = 0.75
    with open('TrainsetTugas1ML.csv', 'rt') as csvfile:
        print('1. Please wait ...')
        # Get Data
        dataset = readFile(csvfile)
        # Split into learn and train
        learnDataset, trainDataset = splitDataset(dataset,splitRatio)
        print(('Split {0} rows into learn={1} and train={2} rows').format(len(dataset), len(learnDataset), len(trainDataset)))
        # Split learnDataset by output y
        learnSeparatedDataset = separateByClass(learnDataset)
        print(learnSeparatedDataset)


main()
