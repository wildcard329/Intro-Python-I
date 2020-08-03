# Write a program to determine if a number, given on the command line, is prime.

# How can you optimize this program?
# Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC).

num = int(input('input a number'))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'is not a prime number')
            break
    else:
        print(num, "is a prime number")
    
else:
    print(num, "is not a prime number")