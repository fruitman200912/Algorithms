def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(d):
    result = []
    while d:
        value = d.pop(find_min_idx(d))
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))