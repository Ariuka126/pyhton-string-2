# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    hasA=0
    haso=0
    for i in text:
        if i == "@":
            hasA+=1
        elif i==".":
            haso+=1
    if hasA and haso>0:
        return "Valid"
    else:
        return "Invalid"

# Exercise 2
def remove_vowels(text):
    mapping = str.maketrans({"A": "", "E": "", "O": "","I": "","a": "", "e": "", "o": "","i": ""})
    result = text.translate(mapping)
    return result
print(remove_vowels("hello world"))

# Exercise 3
def get_initials(text):
    # Write your code here
    pass

# Exercise 4
def extract_year(text):
    # Write your code here
    pass

# Exercise 5
def is_palindrome(text):
    # Write your code here
    pass

