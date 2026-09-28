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
    mapping = str.maketrans("", "", "aeiouAEIOU")
    return text.translate(mapping)

# Exercise 3
def get_initials(name):
    words = name.split()
    initials = ""
    for word in words:
        initials += word[0].upper() + "."
    return initials

# Exercise 4
def extract_year(text):
    found_year = False

    for word in text.split():
        clean_word = word.strip("!.,?")
        if len(clean_word) == 4 and clean_word.isdigit():
            found_year = clean_word
            break
    return found_year

# Exercise 5
def is_palindrome(text):
    cleaned = ""

    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

