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

# question 19: Cubes till n

# Given an integer n,
# for all non-negative integers i < n, print i³ on a new line.

n = int(input())
for i in range(n):
    print(i**3)

# question 20: Even Squares

# Given an integer n,
# print the square of only even numbers less than n.

n = int(input())
for i in range(n):
    if(i % 2 == 0):
        print(i**2)

# question 21: Squares in Reverse

# Given an integer n,
# print the square of numbers from n-1 to 0 (reverse order).

n = int(input())
for i in range(n-1,-1,-1):
    print(i**2)

# question 22: Century Check

# Given an integer year, return True if:

# the year is divisible by 100

# but not divisible by 400

def is_century_year(year):
    return year % 100 == 0 and year % 400 != 0
print(is_century_yearr(1900))
print(is_century_year(2000))

# question 23: Special year

# Given a year:

# Return True if the year is divisible by 4

# But return False if it is divisible by 8

# Except when it is divisible by 16 (then return True)

def is_special_year(year):
    return year % 16 == 0 or (year % 4 == 0 and year % 8 != 0)
print(is_special_year(12))

# question 24: Fiscal Year Validity

# A year is considered valid if:

# divisible by 5

# not divisible by 25

# unless divisible by 125

def is_valid_fiscal_year(year):
    return year % 125 == 0 or (year % 5 ==0 and year % 25 != 0)
print(is_valid_fiscal_year(2025))

# question 25: Scholarship Eligibility

# Given a student’s marks:

# Eligible if marks ≥ 60

# Not eligible if marks ≥ 90

# Eligible again if marks = 100

def is_scholarship_eligible(marks):
    return marks == 100 or (marks >= 60  and marks < 90)
print(is_scholarship_eligible(75))

# question 26: Print Pattern 

# Given an integer n, print: 1223334444...

n = int(input())
for i in range(1,n+1):
    for _ in range(i):
        print(i,end="")

# question 27: 3D Grid with Sum Constraint

# You are given integers x, y, z, and n.

# Print all coordinates (i, j, k) where:  i + j + k ≤ n

x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = [[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k<=n]
print(result)

# question 28: Square Grid Filter

# You are given an integer n.

# Print all pairs (i, j) where:

# 0 ≤ i ≤ n
# 0 ≤ j ≤ n
# i² + j² ≤ n²

x = int(input())
y = int(input())
n = int(input())
result = [[i,j]for i in range(n+1)for j in range(n+1)if i**2 + j**2 <= n**2]
print(result)

# question 29: Second Lowest Number

# You are given an integer n and a list of n integers.

# Print the second lowest unique value.

n = int(input())
score = list(map(int,input().split()))
orig_value = set(score)
if len(orig_value)<3:
    print("not enough unique values")
else:
    min_value = min(orig_value)
    orig_value.remove(min_value)
    print(min(orig_value))

# question 30: Third Highest Number

# You are given n integers.

# Print the third highest unique value.

n = int(input())
score = list(map(int,input().split()))
orig_val = set(score)
if len(orig_val)<3:
    print("not emough value to print")
else:
    max_val = max(orig_val)
    orig_val.remove(max_val)
    max_val = max(orig_val)
    orig_val.remove(max_val)
    print(max(orig_val))

# question 31: You are given n students.
# Each student has a name and 3 subject marks.

# Store the data in a dictionary and print the average marks of the student whose name is given.

n = int(input())
student_marks = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float , data[1:]))
    student_marks[name] = marks

query_name = input()

avg = sum(student_marks[query_name]) / (len(student_marks[query_name]))
print(f"{avg:.2f}")

# question 32: Given student records with names and 3 marks each,
# print the name of the student with the highest average.

n = int(input())
student_marks = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float,data[1:]))
    student_marks[name] = marks

highest_val = -1
top_student = ""

for name,marks in student_marks.items():
    avg = sum(marks) / len(marks)
    if(avg > highest_val):
        highest_val = avg
        top_student = name
        
print(top_student)

# question 33: Check if a number is automorphic or not.

num = int(input("Enter number: "))

square = num ** 2

if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not Automorphic")

# question 34: Find Second Largest Element (Without Sorting).

nums = [10, 20, 4, 45, 99]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)

# question 35: Student Grade Calculator

def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

grade = calculate_grade(marks)

print("Name:", name)
print("Grade:", grade)

# question 36: Find the highest score from the dictonary.

students {"Aman " : 78,
          "Riya" : 92,
          "Kunal" : 67,
          "Simran" : 88
         }

top_student = None
highest_marks = 0

for name,marks in students.items():
    if(marks > highest_marks):
        highest_marks = marks
        top_student = name

print("Name = ",top_name , ", Marks = ",marks)

# question 37: Given a list of integers, find the second largest element without using the sort() function

numbers = [10, 45, 23, 67, 12]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)

# question 38: Write a program that prints all prime numbers between two given numbers.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

# question 39: Given two integers a and b, generate all pairs (i, j) such that:

# 0 ≤ i ≤ a
# 0 ≤ j ≤ b

# But only include pairs where:
# i+j<5

a = int(input())
b = int(input())

result = [[i,j]
          for i in range(a+1)
          for j in range(b+1)
          if(i+j)<5]
print(result)

# question 40: Given two lists A and B, generate their Cartesian product (a, b) but include only pairs where:
# a × b < 10

A = [1,2,3,4]
B = [2,3,5]

result = [(a, b) for a in A for b in B if a*b < 10]

print(result)

# question 41: Given n integers, find the number that appears most frequently.
            # If multiple numbers have the same frequency, print the smallest number among them.

# Input Format
# 6
# 1 3 2 3 4 1

n = int(input())
nums = list(map(int,input().split()))

max_freq = 0
result = None

for num in nums:
    freq = nums.count(num)
    if freq > max_freq:
        max_freq = freq
        result = num
    elif(freq == max_freq):
        result = min(result,num)
print(result)

# question 42: Given n integers, calculate the sum of all even numbers in the list.
# Sample Input
# 6
# 1 2 3 4 5 6

n = int(input())
nums = list(map(int,input().split()))

sum = 0
for num in nums:
    if(num % 2 == 0):
        sum += num
print(sum)

# question 43:  Create a stack using a list and perform operations:
#1. push x → push element
#2. pop → remove top element
#3. top → print top element
#4. size → print size of stack

n = int(input())
lst = []
for _ in range(n):
    command = input().split()
    if(command[0] == "push"):
        lst.append(int(command[1]))
    elif(command[0] == "pop"):
        if lst:
            lst.pop()
    elif(command[0] == "top"):
        if lst:
            print(lst[-1])
    elif(command[0] == "size"):
        print(len(lst))

# question 44:  You are given a list. Perform operations:
# 1. add x → add element
# 2. even → print all even numbers
# 3. odd → print all odd numbers
# 4. sum → print sum of list

lst = []
n = int(input())
for _ in range(n):
    command = input().split()
    if(command[0] == "add"):
        lst.append(int(command[1]))
    elif(command[0] == "even"):
        for i in lst:
            if(i % 2 == 0):
                print(i)
    elif(command[0] == "odd"):
        for i in lst:
            if(i % 2 != 0):
                print(i)
    elif(command[0] == "sum"):
       print(sum(lst))

# question 45: Given an integer n and n space-separated integers, create a tuple t.
#              Print the sum of elements and the hash of the tuple.

n = int(input())
create_lst = map(int,input().split())
t = tuple(create_lst)
print(sum(t))
print(hash(t))

# question 46: Given n integers, store them in a tuple t.
#              Print the number of unique elements in the tuple.

n = int(input())
t = tuple(map(int,input().split()))
unique_count = len(set(t))
print(unique_count)

# question 47: Create a tuple t from input.
               # Print how many times a given number x appears in the tuple.

n = int(input())
t = tuple(map(int,input().split()))
x = int(input())
count = 0
for i in t:
    if(i == x):
        count += 1
print(count)

# question 48: Create a tuple t and print the difference between the maximum and minimum elements.

n = int(input())
t = tuple(map(int,input().split()))
max_num = max(t)
min_num = min(t)
print(max_num - min_num)

# question 49: write a function: 
            # Given a string, reverse each word individually while maintaining the original word order.

def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
        
    return " ".join(reversed_words)

s = input()
print(reverse_words(s))

# question 50: Given a string, count how many uppercase and lowercase letters are present.

str = input()
uppercase_count = 0
lowercase_count = 0
for ch in str:
    if ch.isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1
print(uppercase_count)
print(lowercase_count)

# question 51: Replace all spaces in the string with hyphens (-).

str = input()
print(str.replace(" ","-"))

# question 52: Given a string, remove duplicate characters while preserving the order of first occurrence.

str = input()
result = " "
for ch in str:
    if ch not in result:
        result += ch
print(result)

# question 52: Given a string of space-separated words, count how many words are present.

str = input().split()
count = 0
for word in str:
    count += 1
print(count)

# question 53: Given a string, remove duplicate words while maintaining the original order.

str = input().split()
result = []
for word in str:
    if word not in result:
        result.append(word)
print(" ".join(result))

# question 54: Given a string, count how many substrings consist only of vowels (a, e, i, o, u).

s = input()
vowles = "aeiouAEIOU"
count = 0
current = 0

for ch in s:
    if ch in vowles:
        current += 1
        count += current
    else:
        current = 0
print(count)

# question 55: Given a string and a character, count how many times the character appears in the string.

s = input()
c = input()
count = 0
for ch in s:
    if ch in c:
        count += 1
print(count)
