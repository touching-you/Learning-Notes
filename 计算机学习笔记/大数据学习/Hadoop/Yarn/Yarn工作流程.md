YARN的工作流程可以大致分为以下几个步骤：

1. **应用程序提交**：
   应用程序提交是启动YARN工作流程的第一步。应用程序可以通过命令行或API提交给YARN，应用程序的描述包括应用程序类型、启动脚本、输入输出路径等。
2. **ResourceManager分配资源：**
   ResourceManager会对应用程序进行资源分配，包括内存、CPU、磁盘等，根据应用程序需求来分配。ResourceManager会监控集群的资源使用情况，保证分配的资源不超过集群的总容量。
3. **NodeManager启动容器：**
   ResourceManager将分配的资源信息发送给NodeManager，NodeManager将启动一个或多个容器来承载应用程序。容器是运行应用程序的基本单位，它包含了应用程序需要的所有资源和环境。
4. **应用程序执行：**
   一旦容器启动，应用程序就可以在其中运行。应用程序可以是各种类型，例如MapReduce、Spark等。NodeManager会监控容器的运行情况，并将容器的状态发送给ResourceManager。
5. **ResourceManager监控应用程序：**
   ResourceManager会监控应用程序的状态，包括容器的状态、进度等。如果发现某个容器失败，ResourceManager会尝试重新启动容器。
6. **应用程序完成：**
   一旦应用程序完成，它将向ResourceManager发送完成信号。ResourceManager会将应用程序的输出数据存储到指定的位置，并向客户端发送完成消息。

总的来说，**YARN的工作流程是将应用程序提交给ResourceManager，ResourceManager对资源进行分配，NodeManager启动容器，应用程序在容器中运行，ResourceManager监控应用程序的状态，应用程序完成后输出数据存储到指定位置**。YARN通过这些步骤提供了一个高效、灵活的资源管理和任务调度框架