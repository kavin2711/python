n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True  # Assume the number is prime

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
