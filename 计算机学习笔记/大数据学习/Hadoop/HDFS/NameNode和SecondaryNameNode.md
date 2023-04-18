在Hadoop的HDFS中，NameNode是**主节点**，负责管理文件系统命名空间并控制客户端对文件的访问。Secondary NameNode是一个**辅助节点**，定期从NameNode检查点文件系统元数据并创建新的检查点镜像。

以下是NameNode和Secondary NameNode在HDFS中的工作方式：

1. 客户端应用程序向NameNode发送文件系统请求，例如创建新文件或读取现有文件。
2. NameNode响应所请求的文件系统元数据，包括文件数据块的位置。
3. 客户端应用程序通过与存储文件数据块的DataNode直接通信来访问文件数据。
4. 定期，Secondary NameNode会联系NameNode并请求当前文件系统元数据的副本。
5. NameNode创建一个包含当前文件系统元数据的新检查点镜像，并将其发送给Secondary NameNode。
6. Secondary NameNode将新的检查点镜像应用于其本地文件系统元数据副本。
7. 如果NameNode失败，Secondary NameNode可以使用其本地元数据副本帮助新的NameNode重新启动和恢复文件系统。
8. Secondary NameNode还监视NameNode的日志文件，并将其应用于其本地元数据副本以保持其最新状态。

总的来说，Secondary NameNode为NameNode提供备份，并有助于防止NameNode故障时的数据丢失。它还通过维护当前的文件系统元数据副本来帮助减少重新启动NameNode所需的时间。

> 因为Hadoop可以采用追加数据方式记录数据，因此可以采用fsimage存储Namenode元数据，利用edits记录操作记录（追加记录）。Secondary NameNode中只记录edits的副本文件，而NameNode中还会记录最新操作记录，这样可以在Namenode出错后快速恢复。
>
> ![image-20230318095456917](G:\编程学习\大数据学习\Hadoop\HDFS\images\image-20230318095456917.png)