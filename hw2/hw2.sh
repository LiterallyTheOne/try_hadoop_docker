hdfs dfs -rm -r /hw2_output

yarn jar $HADOOP_STREAMING_JAR -files mapper_2.py,reducer_2.py \
    -mapper "python mapper_2.py" \
    -reducer "python reducer_2.py" \
    -numReduceTasks 1 -input /hw2 -output /hw2_output
