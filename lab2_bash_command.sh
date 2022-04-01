# 20 từ được nhắc nhiều nhất tweet elonmusk
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk  -output /user/hdoop/data/elonmusk_tweet_output-top20-word!  -cmdenv LC_CTYPE=vi_VN.UTF-8

# 
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk/elon_tweet.csv  -output /user/hdoop/data/elonmusk_tweet_time_elon_tweet_most -cmdenv LC_CTYPE=vi_VN.UTF-8

# 10 tài khoản được ElonMusk nhắc nhiều nhất
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk_tweet  -output /user/hdoop/data/10_account_elonmusk_tweet_much -cmdenv LC_CTYPE=vi_VN.UTF-8

# 20 từ được ElonMusk nói trong tweet nhiều nhất
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar  -file mapper.py -mapper mapper.py  -file reducer.py -reducer reducer.py  -input /user/hdoop/data/elonmusk_tweet  -output /user/hdoop/data/20-word-elon-tweet-much -cmdenv LC_CTYPE=vi_VN.UTF-8


/user/hdoop/data/elonmusk_tweet


hdfs dfs -mkdir -p data/lab3

hdfs dfs -chmod -R 777 /user/hdoop/data

