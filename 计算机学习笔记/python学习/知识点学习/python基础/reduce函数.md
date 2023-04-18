**`reduce()`** 函数用于对序列中的元素进行累积操作，将序列中的所有元素通过一个指定的函数进行计算，并返回最终的结果。该函数需要两个参数：一个函数和一个可迭代对象。

> reduce函数可以设置`initializer`参数 ，用于指定累加器的初始值

```
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

//initializer
product = reduce(lambda x, y: x * y, numbers,10)
print(product)  # 130

```

