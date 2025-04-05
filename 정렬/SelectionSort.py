def sel_sort(d):
    n = len(d)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1,n):
            min_idx = j if d[j] < d[min_idx] else min_idx
        d[i], d[min_idx] = d[min_idx], d[i]
d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)