### **1.YARN** (Yet Another Resource Negotiator)的基础架构由两个主要组件组成：**ResourceManager**和**NodeManager**。

**ResourceManage**r：
ResourceManager是YARN的中心组件，**负责协调整个集群中的资源**。它运行在主节点上，并接收来自客户端的资源请求。ResourceManager跟踪所有节点上可用的资源，并决定将哪些资源分配给哪个应用程序。ResourceManager还管理所有正在运行的应用程序，并为它们分配资源。此外，它还**监视应用程序的状态，例如CPU使用率、内存使用率和容器启动状态**。

**NodeManager**：
NodeManager运行在每个工作节点上，它的主要作用是**管理该节点上的资源**。NodeManager跟踪可用的资源，例如CPU、内存和磁盘，然后与ResourceManager通信以获取分配给该节点的任务。NodeManager启动和监视容器，以便应用程序可以运行在分配给它们的资源上。

在YARN的基础架构中，**应用程序通常是通过一个或多个容器运行的**。**每个容器都是一组资源，包括CPU、内存和磁盘，它们被分配给单个应用程序实例**。容器的创建和销毁由NodeManager管理。容器是可插拔的，这意味着可以运行不同类型的应用程序，包括MapReduce、Spark等。

总的来说，YARN的基础架构是一个分布式系统，通过ResourceManager和NodeManager协调和管理集群中的资源，提供了一个灵活的平台来运行不同类型的应用程序。

### 2.Container和ApplicationMaster再Yarn中的关系

在 Yarn 中，**Container（容器）是一个抽象的概念，用于运行应用程序的任务**。每个容器都包含了一个独立的应用程序运行环境，包括代码、依赖项和运行时资源。在 Yarn 中，Container 是由 NodeManager 启动的，并由 ApplicationMaster 管理。

ApplicationMaster 是 Yarn 中的一个重要组件，它**负责协调应用程序的运行，包括获取资源、管理任务、监控任务状态和任务之间的依赖关系等**。**每个应用程序都有一个 ApplicationMaster**，它运行在一个容器中，并与 ResourceManager 通信以获取资源。一旦 ApplicationMaster 获取了足够的资源，它开始协调各个任务的执行，并在任务完成后将应用程序的状态更新为“完成”。

在 Yarn 中，**ApplicationMaster 和容器之间存在一对多的关系**。一个 ApplicationMaster 可以管理多个容器，每个容器负责运行一个或多个任务。ApplicationMaster 还负责监控容器的状态，如果容器异常退出，它会重新启动容器并重新分配任务。

总之，Yarn 通过将应用程序拆分为多个任务，并将任务分配给各个容器中运行，实现了资源的动态管理和任务的并行执行，从而提高了集群的利用率和可伸缩性。
