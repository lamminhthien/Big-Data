hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
 -file mapper.py -mapper mapper.py \
 -file reducer.py -reducer reducer.py \
 -input /user/hdoop/data/elonmusk_tweet \
 -output /user/hdoop/data/elonmusk_tweet_output -cmdenv LC_CTYPE=vi_VN.UTF-8

/user/hdoop/data/twitter-following

