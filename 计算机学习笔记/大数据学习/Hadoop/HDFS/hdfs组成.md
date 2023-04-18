#### HDFS组成

1. NameNode

   它就是Master，主要负责管理DataNode

   - 管理HDFS的名称空间；
   - 配置副本策略；
   - 管理数据块的映射信息；
   - 处理客户端的读写请求。

2. DataNode

   它就是Slav，主要负责执行NameNode下达的指令操作并且存储数据信息

   - 存储实际的数据块；
   - 执行数据块的读/写操作。

3. Secondary NameNode

   并非NameNode的热备，当Name Node挂掉的时候，并不能马上替换NameNode并提供服务

   - 辅助NameNode，并分担其工作量，比如定期何必跟Fsimage和Edits，并推送给NameNode；
   - 在紧急情况下可以辅助恢复NameNode。

4. Client：客户端

   - 文件切分：文件上传HDFS时，Client将文件切分成一个个文件块；
   - 与NameNode交互，获取文件的位置信息；
   - 与DataNode交互，读取或者写入数据；
   - Client提供一些命令来管理HDFS，比如Name Node格式化；
   - Client可以通过一些非命令来访问HDFS，比如对HDFS增删改查操作。