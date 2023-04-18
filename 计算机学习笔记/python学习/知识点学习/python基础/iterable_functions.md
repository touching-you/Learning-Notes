**`zip()`**可以将多个可迭代对象中对应位置的元素打包成一个元组，然后返回这些元组组成的**迭代器**。

> `zip()`函数可以接受不等长的迭代对象，然后将对象按短截断，再一一对应。

```python
x = [1, 2, 3]
y = ['a', 'b', 'c']
z = zip(x, y)
for i in z:
    print(i)
************
(1, 'a')
(2, 'b')
(3, 'c')
```

此外，**`zip()`** 函数还可以与解压符号 `*` 结合使用，用于将已经被 zip 函数打包的元素重新解压回来。

```
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
unzipped = zip(*zipped)
print(list(unzipped))
***************
[(1, 2, 3), ('a', 'b', 'c')]
```

**`map()`**可以将一个函数应用于一个可迭代对象的每个元素，并返回一个由应用了函数后的元素组成的迭代器。

```python
def square(x):
    return x ** 2

x = [1, 2, 3, 4, 5]
y = map(square, x)
print(list(y))
**************
[1, 4, 9, 16, 25]
```

**`filter()`**函数可以将一个函数应用于可迭代对象，利用函数对可迭代对象进行过滤，然后返回符合条件的元素。

```python
my_list = [1, 2, 3, 4, 5, 6]
filtered_list = filter(lambda x: x % 2 == 0, my_list)
print(list(filtered_list)) 
*****************
[2, 4, 6]

```

**`any() and all()`**函数用于判断满足条件的元素，返回一个bool结果，不过前者只需要一个满足条件即可，后者需要所有元素都满足条件。

```
my_list = [1, 2, 3, -4, 5, 6]
print(any(num < 0 for num in my_list))  # True

my_list = [1, 2, 3, 4, 5, 6]
print(all(num > 0 for num in my_list))  # True

```

