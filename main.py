def getTextContents():
    with open('books/frankenstein.txt', 'r') as file:
        content = file.read()

    return content

def countWords(content):
    words = content.split()
    
    return len(words)

def countCharacters(content):
    letter_counts = {}
    for letters in content:
        letter_cased = letters.lower()
        if letter_cased in letter_counts:
            letter_counts[letter_cased] = letter_counts[letter_cased] + 1
        else:
            letter_counts[letter_cased] = 1

    return letter_counts


print(countCharacters(getTextContents()))
