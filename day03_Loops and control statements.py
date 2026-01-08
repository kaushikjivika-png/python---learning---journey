# Python:

# Day 3: Loops and Control statements
# Topics covered: While loop, For loop, Break statement, Continue statement, Range, Pass statement.

# 1. While loop:
# Syntax:               while condition:
#                               code to be executed

# Print numbers from 1 to 10.

i = 1
while i<=10:
    print(i)
    i += 1

# print even numbers from 1 to 20.

i = 2
while i<=20:
    print(i)
    i += 2

# 2.For loop:
# Syntax:                  for condition:
#                               code to be executed

# print characters of a string using for loop.

name = "jivika"
for ch in name:
    print(ch)

# program to count vowles.

text = "education"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

# 3.Break statement:

# program to stop loop when number is 5.

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 4.Continue statement:

# program to skip number 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 5.Range:

# program to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

# program to print even numbers from 2 to 20.

for i in range(2, 21, 2):
    print(i)

# 6.Pass statement:

# program to pass inside loop.

for i in range(1, 6):
    if i == 3:
        pass
    print(i)



