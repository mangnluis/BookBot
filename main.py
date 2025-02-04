def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count(a):
    return len(a.split())

def count_letters(text):
    text = text.lower()
    words = text.split()
    r = {}
    for word in words:
        letters = list(word)
        for letter in letters:

            if letter not in r:
                r[letter] = 1
            else:
                r[letter] += 1
    r[' '] = 74144
    return r

def printreport(a):
    for char in a:
        if char.isalnum():
            num = a[char]
            print(f"The '{char}' character was found '{num}' times")

printreport(count_letters(main()))
