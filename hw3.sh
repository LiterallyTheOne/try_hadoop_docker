hdfs dfs -rm -r /app/hw3_output

yarn jar $HADOOP_STREAMING_JAR -files mapper_reducer_3.py,combiner_3.py \
    -mapper "python mapper_reducer_3.py" \
    -reducer "python mapper_reducer_3.py" \
    -combiner "python combiner_3.py" \
    -numReduceTasks 1 -input /hw2 -output /app/hw3_output
