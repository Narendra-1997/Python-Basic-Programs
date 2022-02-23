def prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("is not a prime ")
            break
        else:
            print("is a prime number")

prime(5)
