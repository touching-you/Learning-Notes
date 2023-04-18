# KMP

```python
def build_next(pat):
    next = [0]
    prefix_len = 0
    i = 1 
    while(i < len(pat)):
        if pat[prefix_len] == pat[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = nex[prefix_len - 1]
    return next

def search(string , pat):
    next = build_next(pat)
    
    i = 0
    j = 0
    while(i < len(string)):
        if string[i] == pat[j]:
            i += 1
            j += 1
        elif j > 0:
            j = next[j - 1]
        else:
            i += 1
        if j== len(pat):
            return i-j
```