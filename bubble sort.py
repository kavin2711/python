x = [1, 2, 9, 4, 8, 5, 7, 6, 3, 10]
y = len(x)

for j in range(y - 1):
    for i in range(y - 1): 
        if x[i] > x[i + 1]:
        
            temp = x[i]
            x[i] = x[i + 1]
            x[i + 1] = temp

print(x)


    

