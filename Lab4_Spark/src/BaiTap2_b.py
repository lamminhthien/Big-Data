# Khai báo thư viện
import os, shutil
from pyspark import SparkContext

# tạo đối tượng Spark context 
sc = SparkContext("local", "Text processing with PySpark")

lines = sc.textFile("/home/hung/Downloads/gutenberg")

# split the lines into separated words
words = lines.flatMap(lambda line: line.split(" "))

# count the occurrence of each word
wordFrequencies = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a + b)