l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
x=int(input("Enter the number to find its index: "))
a=0
for i in l :
    if i == x:
        print("The index of", x, "is", a)
        break
    a += 1
else:
    print("The number", x, "is not in the list.")
    