hdfs dfs -rm -r /only_ip_output

yarn jar $HADOOP_STREAMING_JAR -files only_print.py \
    -D stream.map.output.field.separator=. \
    -D stream.num.map.output.key.fields=2 \
    -D stream.reduce.output.field.separator=. \
    -D stream.num.reduce.output.key.fields=2 \
    -mapper "python only_print.py" \
    -reducer "python only_print.py" \
    -numReduceTasks 1 -input /ip_2/ip_2.txt -output /only_ip_output

hdfs dfs -cat /only_ip_output/*
