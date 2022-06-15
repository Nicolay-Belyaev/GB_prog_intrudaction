Arr = [90, 40, 1, 1, 10000000, 29, 71, 0]
accumulator = 0
min_i = 0
max_i = 0
for i in range(1, len(Arr)): 
    if Arr[i] < Arr[min_i]:
        min_i = i
    if Arr[i] > Arr[max_i]:
        max_i = i
if min_i < max_i:                               # если минимальный элемент находится в массиве до максимального...
    for j in range (min_i+1, max_i):
        accumulator += Arr[j]                   # ... просто складываем находящиеся между ними элементы,
else:                                           # в противном случае, делаем тоже самое, но идем по массиву в обратную сторону
    for j in range(min_i-1, max_i,-1):
        accumulator += Arr[j]
print(accumulator)