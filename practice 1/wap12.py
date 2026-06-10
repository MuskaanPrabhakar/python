#Print the following pattern using nested loops (n=5, take n as input)
for i in range(1,int(input("Enter number of lines you want to print for pattern inverted triangle: "))+1):
    print("*"*i)
n=int(input("Enter number of lines you want to print for pattern diamond: "))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(i+(i-1)))
n=int(input("Enter number of lines you want to print for pattern hollow trainagle: "))
k =-1
for i in range(n,0,-1):
    print(" "*(i-1)+"*"+" "*k+"*"*(i!=n))
    k+=2