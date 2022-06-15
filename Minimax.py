Arr = [1, 2, 2, 2, 1]
min_i = 0
max_i = 0
for i in range(1, len(Arr)):  # интересно, что обе проверки корректно работают в одном цикле
    if Arr[i] < Arr[min_i]:
        min_i = i
    if Arr[i] > Arr[max_i]:
        max_i = i
print(min_i, max_i)

#мимо пробегал Оккам с бритвой:
print(Arr.index(min(Arr)), Arr.index(max(Arr)))