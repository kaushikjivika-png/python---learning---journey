# Python:

# question 1:  Program to find square and cube of a number.

num = int(input("Enter a number: "))

print("Square =", num ** 2)
print("Cube =", num ** 3)

# question 2:  Program to check positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# question 3: Program to swap two number.  1.  using third variable , 2. without using third variable.

a = int(input("Enter a: "))                 # without third variable
b = int(input("Enter b: "))

a, b = b, a

print("a =", a)
print("b =", b)

a = int(input("Enter value of a: "))        # with using third variable
b = int(input("Enter value of b: "))

temp = a      # store value of a in temp
a = b         # assign value of b to a
b = temp      # assign value of temp to b

print("After swapping:")
print("a =", a)
print("b =", b)

# question 4: Program to check leap year.

year = int(input("enter year : "))
if(year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year")
elif(year % 400 == 0 and year % 100 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not leap year")

# question 5: Program to check vowel or consonant.

ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# question 6: Program to reverse a number.

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)

# question 7: Program to check the number is palindrome or not.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

# question 8: Program to print the sum of first n natural numbers.

num = int(input("enter number : "))
sum = 0
i = 1
while i<=num:
    sum += i
    i += 1
print("sum = ",sum)

# question 9: Program to print Fibonacci series up to n terms.

n = int(input("enter number of terms :"))
a,b = 0,1
count = 0
while count < n:
    print(a,end= " ")
    next_term = a + b
    a = b
    b = next_term
    count += 1                    

# question 10: Program to find the factorial of a number.

num = int(input("enter number : "))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print("factorial =",factorial)                   

# question 11: Function to check whether a number is prime or not
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# question 12: Program to check the number of vowles in a string.

name = "Jivika"
vowles = "aeiouAEIOU"
count = 0
for char in name:
    if char in vowles:
        count += 1
print("Number of vowles in",name,"is",count)

# queston 13: Given an integer n:

# If n is odd, print Risk

# If n is even and between 10 and 50 (inclusive), print Audit

# If n is even and greater than 50, print Tax

n = int(input())

if n % 2 != 0:
    print("Risk")
elif 10 <= n <= 50:
    print("Audit")
else:
    print("Tax")

# question 14: Given an integer n:

# If n is negative → print Invalid

# If n is 0 → print Zero Case

# If n is positive and even → print Positive Even

# If n is positive and odd → print Positive Odd

n = int(input())

if n == 0:
    print("Zero Case")
elif n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Invalid")

# question 15: Three Integers Arithmetic

# You are given three integers a, b, and c.

# Print:

# Sum of all three numbers

# Average of the three numbers (integer value)

# Maximum among the three numbers

a = int(input())
b = int(input())
c = int(input())
print("SUM : ",a + b + c)
print("AVERAGE : " ,((a+b+c)//3))
print("MAXIMUM : ",max(a,b,c))

# question 16: Even–Odd Difference

# You are given two integers a and b.

# If both numbers are even, print their sum

# If both numbers are odd, print their product

# Otherwise, print their difference (a - b)

a = int(input())
b = int(input())
if(a % 2 == 0 and b % 2 == 0):
    print("SUM : ",a + b)
elif(a % 2 != 0 and b % 2 != 0):
    print("MULTIPLICATION :",a * b)
else:
    print("DIFFERENCE :", a - b)

# question 17: Division with Swap

# You are given two integers a and b.

# First, print integer division of a // b

# Then swap a and b

# Print float division of the swapped values

a = int(input())
b = int(input())
if(b != 0):
    print(a // b)
else:
    print("cannot divide by zero")
a,b = b,a                            # swap values
if(b != 0):
    print(a / b)
else:
    print("cannot divide by zero")

# question 18: Average Calculator

# You are given two integers a and b.

# Print:

# Integer average of a and b

# Float average of a and b

a = int(input())
b = int(input())

print((a + b) // 2)   # integer average
print((a + b) / 2)    # float average
