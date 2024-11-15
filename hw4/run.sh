mapper="mapper.py"
reducer="reducer.py"
input_file="/hw2"
output_file="/app/hw4_output"

hdfs dfs -rm -r "$output_file"

yarn jar $HADOOP_STREAMING_JAR \
    -files "$mapper,$reducer" \
    -mapper "python $mapper" \
    -reducer "python $reducer" \
    -numReduceTasks 1 \
    -input "$input_file" \
    -output "$output_file"

hdfs dfs -cat "$output_file/*"
