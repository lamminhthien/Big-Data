hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk  -output /user/hdoop/data/elonmusk_tweet_output-top20-word!  -cmdenv LC_CTYPE=vi_VN.UTF-8

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk/elon_tweet.csv  -output /user/hdoop/data/elonmusk_tweet_time_elon_tweet_most -cmdenv LC_CTYPE=vi_VN.UTF-8



hdfs dfs -mkdir -p data/lab3

hdfs dfs -chmod -R 777 /user/hdoop/data

