# Python

# question 26: Print Pattern 

# Given an integer n, print: 1223334444...

n = int(input())
for i in range(1,n+1):
    for _ in range(i):
        print(i,end="")