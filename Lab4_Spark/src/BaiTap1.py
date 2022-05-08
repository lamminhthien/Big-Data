from gc import collect
import os, shutil
from pyspark import SparkContext
# Create a output file if it is not exist
try:
	f = open("BaiTap1-output.txt","x")
except:
	# If exist file, change file mode to write
	f = open("BaiTap1-output.txt","w")


# create Spark context with necessary configuration
sc = SparkContext("local", "Text processing with PySpark Example")

# read data from text file into lines  
lines = sc.textFile("/mnt/d/Code/Big-Data/Lab4_Spark/src/apache_log.log").cache()

# # Filter lines contain 'error' and count
# errorLinesCount = lines.filter(lambda s: 'error' in s).count()
# print('There are'+ str(errorLinesCount) + 'contain error')

# Print lines contain 'error' 
for element in lines.filter(lambda s: 'error' in s).collect():
	print(element)
	f.write(element + '\n')