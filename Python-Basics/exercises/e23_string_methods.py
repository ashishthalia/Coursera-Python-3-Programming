# All methods on strings are NON-MUTATING because strings are immutable.
# They all create new strings in memory.

# upper() and lower()
s = "hello"
t = s.upper()
print(s, t)  # hello HELLO
# If we want to change the string s is pointing to, we have assign the new string generated by upper() to s itself.
s = s.upper()
print(s)  # HELLO
s = s.lower()
print(s)  # hello

# counting the number of times a letter/substring appears in a string
print(s.count("l"))  # 2
print(s.count("ello"))  # 1

# replace() creates a new string where all occurrences of a substring are replaced by another substring
t = s.replace("l", "t")
print(s, t)  # hello hetto
s = s.replace("ll", "oo")
print(s, t)  # heooo hetto

# strip() gets rid of all spaces at the beginning and end of a string, leaving only the characters in the middle
s = "    hi there what up    "
print("***" + s.strip() + "***")  # ***hi there what up***

# finding out the index where the first appearance of a substring occurs
print(s.index("hi"))  # 4

# concatenation (+) creates a new string by joining two
s = "ok " + "fine"
print(s)  # ok fine

# multiplication (*) creates a new string by joining the same string with itself a number of times
s = "ok" * 5
print(s)  # okokokokok
