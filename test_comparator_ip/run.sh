mapper="only_print.py"
reducer="only_print.py"
input_file="/c_ip/c_ip.txt"
output_file="/comparator_output"

hdfs dfs -rm -r "$output_file"

yarn jar $HADOOP_STREAMING_JAR \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator=. \
    -D mapreduce.partition.keycomparator.options="-k2,2 -k3,3r" \
    -files "$mapper" \
    -mapper "python $mapper" \
    -reducer "python $reducer" \
    -numReduceTasks 1 \
    -input "$input_file" \
    -output "$output_file"

hdfs dfs -cat "$output_file/*"
