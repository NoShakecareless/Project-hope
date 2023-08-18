astring = "Hello world!"
astring2 = 'Hello world!'
print("single quotes are ' '")

print(len(astring))
print(astring.index("l"))
print(astring[3:7])
print(astring[3:7:3])   # [start:stop:step]

print(astring[::-1])    # reverse string

print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with something
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list
afewwords = astring.split(" ")
print(afewwords)

# Exercise
s = "Strings are awesome!"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])     # Start to 5
print("The next five characters are '%s" % s[5:10])     # 5 to 10
print("The thirteenth character is '%s'" % s[12])   # Just number 12
print("The characters with odd index are '%s'" % s[1::2])   # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])     # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())
