mapper="mapper.py"
reducer="reducer.py"
input_file="/hw2"
output_file="/app/hw4_output"

hdfs dfs -rm -r "$output_file"

yarn jar $HADOOP_STREAMING_JAR \
    -D stream.map.output.field.separator="\t" \
    -D mapreduce.partition.keypartitioner.options="-k4,4" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options="-k4,4" \
    -D stream.num.map.output.key.fields=4 \
    -files "$mapper,$reducer" \
    -mapper "python $mapper" \
    -reducer "python $reducer" \
    -numReduceTasks 2 \
    -input "$input_file" \
    -output "$output_file" \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat "$output_file/part-00000"
