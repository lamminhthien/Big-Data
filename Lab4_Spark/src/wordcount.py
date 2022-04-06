import os, shutil
from pyspark import SparkContext

if __name__ == "__main__":
	# create Spark context with necessary configuration
	sc = SparkContext("local", "Text processing with PySpark Example")

	# read data from text file into lines  
	lines = sc.textFile("/mnt/d/Code/Big-Data/Lab2_WordCount/data/gutenberg")

	# split the lines into words
	words = lines.flatMap(lambda line: line.split(" "))

	# count the occurrence of each word
	wordFrequencies = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

	# Sort the result decreasing by number count of word
	wordFrequencies = wordFrequencies.sortBy(lambda x:x[1],ascending=False)

	# save the set of <word, frequency> to disk
	savingPath = "/home/hdoop/gutenberg-result-pyspark"

	# if os.path.isdir(savingPath):
	#     shutil.rmtree(savingPath, ignore_errors=True)
	# wordFrequencies.saveAsTextFile(savingPath)
	print(wordFrequencies)

