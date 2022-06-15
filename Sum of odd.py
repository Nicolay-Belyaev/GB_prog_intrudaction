Arr = [1, 2, 1, 5]
accumulator = 0
for i in range(0, len(Arr)):
    if Arr[i]%2 == 1:
        accumulator += Arr[i]
print(accumulator)