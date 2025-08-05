i=int(input("enter number of lines desired:"))
blank= i-1
starr=1
for k in range(i):
    print(blank*" ",starr*"*",blank*" ")
    blank-=1
    starr+=2

