phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook2 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook2)

# Iterating over dictionaries
for name, number in phonebook2.items():
    #    print(f"Phone number of %s is %d" % (name, number))
    print(f"Phone number of {name} is {number}")

# Removing a value
del phonebook2["John"]
print(phonebook2)
phonebook.pop("John")
print(phonebook)

# Exercise
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781, "Jake": 938273443}
# your code goes here
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")