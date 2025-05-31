










import array as arr

# Integer array example
a = arr.array('i', [1, 2, 3])
print("Integer Array before insertion:", *a)

a.insert(1, 4)  # Insert 4 at index 1
print("Integer Array after insertion:", *a)