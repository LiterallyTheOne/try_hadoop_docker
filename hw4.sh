hdfs dfs -rm -r /app/hw4_output

yarn jar $HADOOP_STREAMING_JAR -files mapper_4.py,reducer_4.py \
    -mapper "python mapper_4.py" \
    -reducer "python reducer_4.py" \
    -numReduceTasks 1 -input /hw2 -output /app/hw4_output
