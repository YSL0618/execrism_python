
text = "1 2 3\n4 5 6\n7 8 9\n10 11 12"
lines = text.splitlines()
print(lines)
array = list(map(lambda row: list(map(int, row.split())), text.splitlines()))
print(array)
print(array[3][1])
print(array[1])
print([row[2] for row in array])
