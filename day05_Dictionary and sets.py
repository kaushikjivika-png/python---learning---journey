# Python:

# Day 4: Python Dictionary and sets
# Topic covered: Dictionary, Nested dictionary, Functions of dictionary, Set, Set functions, example questions

# 1. Dictionary:

# dictonary is a in-built datatype that stores data in key-value pair.
# they are mutable and dont allow duplicate dictonaries keys.
# dictonary is written in the curly brackets{}.
# separate every key:value by comma(,).
# syntax of print null dictonary{}.

# example:
dict = {
    "name" : "jiya",
    "age" : 20,
    "class" : "under graduation",
}
print(dict)

dict["money"] = 3500
print(dict)

# 2. Nested dictonary:

# it is a dictonary that contains another dictonary inside it.

# example:
students = {
    "student1": {
        "name": "Aman",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Riya",
        "age": 21,
        "marks": 90
    }
}
# Accessing values
print(students["student1"]["name"])
print(students["student2"]["marks"])

# 3. functions in dictonary:

""" 1-dict.keys(). #it returns all the key values from the dictonary.
    2-dict.values(). #it returns all the values from the dictonary.
    3-dict.items(). #it returns all the key-value pairs from the dictonary.
    4-dict.get("key"). #it returns the value of the key.
    5-dict.update({"key":"value"}). #it updates the dictonary with new key-values.
    6-dict.pop("key"). #it removes the key-value pair from the dictonary."""
 
# 4. Set:

# set is a in-built datatype that stores unique values.
# it is mutable and unordered collection of items.
# set is written in curly brackets{}.
# syntax of set is {value1,value2,value3}.

# example:
fruits = {"apple","banana","orange"}
print(fruits)
print(type(fruits))

# 5. Set functions:

"""1-set.add("value"). #it adds the value in the set.
   2-set.remove("value"). #it removes the value from the set.
   3-set.clear(). #it clears the set.
   4-set.pop(). #it removes the random value from the set.
   5-set.union(set2). #it combines two sets.
   6-set.intersection(set2). #it returns the common values from the two sets."""

# Questions:

# 1. program to store following word - meaning in python dictionary.
           # table: "a piece of furniture" ,"list of facts and figures", 
           # cat : "a small animal"

word = {
    "table" : "a piece of furniture " "list of facts and figures",
    "cat" : "a small animal",        
}
print(word)

# 2. you are given a list of subject of students. Assume 1 class is required for 1 subject. How many classroom are needed by all students.
#   "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c".

subjects = {"python","java","c++","javascript","java","python","java","c++","c"}
print(len(subjects))


