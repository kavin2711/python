def fibonacci (x):
    for i in range(1,x):
     n.append(n[i-1]+n[i])
    print(n)
n=[0,1]
x=int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci(x-1)