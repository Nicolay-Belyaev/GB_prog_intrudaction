Arr = [0, 1, 2, 3, 4, 5, 10]
Help = 0
for i in range(0, (len(Arr)//2)):
    Help = Arr[i]
    Arr[i] = Arr[len(Arr)-(i+1)]
    Arr[len(Arr)-(i+1)] = Help
print(Arr)