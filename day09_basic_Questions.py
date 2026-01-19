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

    



