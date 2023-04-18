# Simple希尔排序

```python
def shellSort(arr:list)->list:
    gap = len(arr)//2
    while(gap>0):
        for gpStartIndex in range(gap):
            for currentIndex in range(gpStartIndex+gap,len(arr),gap):
                currentNumber = arr[currentIndex]
                preIndex = currentIndex-gap
                while(preIndex>=gpStartIndex and currentNumber<arr[preIndex]):
                    arr[preIndex+gap] = arr[preIndex]
                    preIndex -= gap
                arr[preIndex+gap] = currentNumber
        gap = gap//2
    return arr
```