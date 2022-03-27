hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
 -file mapper.py -mapper mapper.py \
 -file reducer.py -reducer reducer.py \
 -input /user/hdoop/data/twitter-following \
 -output /user/hdoop/data/twitter-following-output -cmdenv LC_CTYPE=vi_VN.UTF-8

/user/hdoop/data/twitter-following

