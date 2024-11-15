hdfs dfs -rm -r /bigram_output

yarn jar $HADOOP_STREAMING_JAR \
    -files mapper.py,reducer.py \
    -D stream.num.map.output.key.fields=2 \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -numReduceTasks 1 \
    -input /bigram \
    -output /bigram_output

hdfs dfs -cat /bigram_output/*
