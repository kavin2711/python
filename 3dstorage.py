empty=""
_3d=[[[empty for _ in range(6)] for _ in range(6)] for _ in range(6)]
print(_3d)
count=0
for i in range(6):
    for j in range(6):
        for k in range(6):
            _3d[i][j][k] =count
            count+=1 
print(_3d)
    
