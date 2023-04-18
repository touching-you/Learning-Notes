HDFS的shell操作



```shell
#启动HDFS
sbin/start-dfs.sh
sbin/start-yarn.sh
#停止HDFS

#创建文件夹
hdfs dfs -mkdir <directory path>

#上传文件
hdfs dfs -put <local file path> <HDFS file path>

#下载文件
hdfs dfs -get <HDFS file path> <local file path>

#列出文件夹中文件
hdfs dfs -ls <directory path>

#删除文件或文件夹
hdfs dfs -rm <HDFS file path>
hdfs dfs -rmdir <HDFS directory path>

#检查文件或文件夹的大小
hdfs dfs -du <HDFS file or directory path>

#读取文件目录
hdfs dfs -cat <HDFS file path>

```

