hdfs dfs -mkdir /ip
hdfs dfs -mkdir /ip_2

hdfs dfs -put -f /app/test_partitioner/ip.txt /ip/ip.txt
hdfs dfs -put -f /app/test_partitioner/ip_2.txt /ip_2/ip_2.txt
