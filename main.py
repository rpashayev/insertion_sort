def insertion_sort(a):
    for i in range(1, len(a)):
        m = a[i]
        for j in range(i, 0, -1):
            if m < a[j-1]:
                a[j]  = a[j-1]
                a[j-1] = m
    return a

a = [2, 3, 1, 7, 5, 4, 9, 6, 11, 10]
print(insertion_sort(a))

b = [200, 123, 111, 117, 250, 124, 139, 206, 110, 210]
print(insertion_sort(b))

