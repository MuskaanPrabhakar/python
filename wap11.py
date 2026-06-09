#Write a program that prints all prime numbers between 1 and 500 using a for loop. Then rewrite it using a list comprehension in a single line. Both must produce identical output.
primes= []
for i in range(2,500):
    if i==2 or i==3:
        primes.append(i)
        print(i)
    elif i%2==1 and (i%3==2 or i%3==1):
        for k in range(len(primes)):
            if i%primes[k]==0:
                break #breaking becoz it's not a prime we find a number that is divisble
            elif primes[k]*primes[k]>i:
                primes.append(i)
                print(i)
                break #here we break becoz we are sure this is prime like in case of 29, we stop at 7 , early optimization 
print(len(primes))
primes = [i for i in range(2, 500) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
print(len(primes))
