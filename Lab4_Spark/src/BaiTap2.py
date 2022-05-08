import os, shutil
from pyspark import SparkContext


# create Spark context with necessary configuration
sc = SparkContext("local", "Text processing with PySpark Example")

# read data from text file into lines  
lines = sc.textFile("/mnt/d/Code/Big-Data/Lab2_WordCount/data/gutenberg")

# split the lines into words
words = lines.flatMap(lambda line: line.split(" "))

# count the occurrence of each word
wordFrequencies = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# Sorted decreasing by value, take only 20 result first
wordFrequencies = wordFrequencies.sortBy(lambda x: x[1],ascending=False).take(20)

# def g(x):
#     print(x)
# wordFrequencies.foreach(g)
print(type(wordFrequencies))
print(wordFrequencies)

# # save the set of <word, frequency> to disk
# savingPath = "/home/hdoop/pyspark-output"

# if os.path.isdir(savingPath):
#     shutil.rmtree(savingPath, ignore_errors=True)
# wordFrequencies.saveAsTextFile(savingPath)