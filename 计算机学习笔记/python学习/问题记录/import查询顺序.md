Python 在导入模块时，会按照以下顺序搜索模块所在的位置：

1. 当前目录：首先搜索**当前执行文件所在的目录或者当前交互式环境的目录**。
2. 环境变量 PYTHONPATH 中指定的目录：如果设置了环境变量 **PYTHONPATH**，则搜索其中指定的目录。
3. **Python 默认的安装路径下的目录**：如果模块没有在当前目录或者 PYTHONPATH 中找到，Python 会接着搜索默认安装路径下的目录。
4. 安装在操作系统的**系统级别的 Python 库路径**：如果还没有找到，则接着搜索操作系统的系统级别的 Python 库路径。