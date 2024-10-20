# Try Hadoop Docker

In this repository we try `Hadoop` in `docker` and
run a simple `map/reduce` on it.

## Usage

### Clone the repository

```shell
git clone https://github.com/LiterallyTheOne/try_hadoop_docker 
```

### Pull

```shell
docker compose pull
```

This codes pulls all the necessary images from docker hub

### Run docker compose

```shell
docker compose up
```

This code builds the `Dockerfile` and runs
a `NameNode` and a `DataNode`

### Connect to `NameNode`

On another terminal, execute the code below:

```shell
docker exec -it namenode /bin/bash
```

This code connects us to `NameNode`,
so we can use the commands needed.

### Move the data to `DataNode`

I have prepared a shell script that `put`s
3 files in `my_data` directory to `/data`
directory on `DataNode`, to run that you can
use the code below:

```shell
sh move_data.sh 
```

So the output of `hdfs dfs -ls /data` would be like below:

```shell
Found 3 items
-rw-r--r--   3 root supergroup         35 2024-10-20 10:16 /data/f1.txt
-rw-r--r--   3 root supergroup         42 2024-10-20 10:16 /data/f2.txt
-rw-r--r--   3 root supergroup         28 2024-10-20 10:16 /data/f3.txt
```

### run mapper alone

```shell
yarn jar $HADOOP_STREAMING_JAR -files mapper.py -mapper "python mapper.py" -input /data -output /output_mapper
```

So the output of `hdfs dfs -ls /output_mapper` would be like below:

```shell
Found 2 items
-rw-r--r--   3 root supergroup          0 2024-10-20 10:19 /output_mapper/_SUCCESS
-rw-r--r--   3 root supergroup          9 2024-10-20 10:19 /output_mapper/part-00000
```

And the output of `hdfs dfs -tail /output_mapper/part-00000` would be like below:

```shell
4	
5	
6
```

### Run Mapper with Reducer

```shell
yarn jar $HADOOP_STREAMING_JAR -files mapper.py,reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -numReduceTasks 1  -input /data -output /output_mapper_reducer
```

So the output of `hdfs dfs -ls /output_mapper_reducer` would be like below:

```shell
Found 2 items
-rw-r--r--   3 root supergroup          0 2024-10-20 10:24 /output_mapper_reducer/_SUCCESS
-rw-r--r--   3 root supergroup          4 2024-10-20 10:24 /output_mapper_reducer/part-00000
```

And the output of `hdfs dfs -tail /output_mapper_reducer/part-00000` would be like below:

```shell
15
```