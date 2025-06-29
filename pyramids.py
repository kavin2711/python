blocks = int(input("Enter the number of blocks: "))
n=0
c=0
for i in range (1,blocks+1):
    if n < blocks:
        n+=i
        c+=1
    else:
        break
        
print("The height of the pyramid:", c)

