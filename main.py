# from stats import
import sys

def getText(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def countWords(path_to_file):
    text = getText(path_to_file)
    return len(text.split())

def countChars(path_to_file):
    text = getText(path_to_file)
    text = text.lower()

    charCount = {}
    for char in text:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    
    return charCount

def generateCharReport(path_to_file):
    chars = countChars(path_to_file)
    sortedChars = sorted(chars)

    report = f"--- Report of {path_to_file} ---\n\n"
    report += f"{countWords(path_to_file)} words found in the document\n\n"
    
    for sChar in sortedChars:
        if sChar.isalpha():
            report += f"The '{sChar}' char was found {chars[sChar]} times.\n"
            report += f"'{sChar}: {chars[sChar]}'"
    report += f"\n--- End Report ---"
    
    return report


def generateWordReport(path_to_file):
    text = getText(path_to_file)
    text = text.lower()
    
    chars = countChars(path_to_file)
    sortedChars = sorted(chars)
    for sChar in sortedChars:
        if not sChar.isalpha() and sChar != " ":
            text = text.replace(sChar, " ")
    
    words = text.split()
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    sWords = sorted(wordCount)

    report = f"--- Report words in {path_to_file} ---\n\n"
    report += f"{len(wordCount)} unique words found in the document\n\n"
    
    for sWords in sWords:
        if wordCount[sWords] > 1000:
            report += f"'{sWords}' was found {wordCount[sWords]} times.\n"
    report += f"\n--- End Report ---"
    
    return report


if __name__ == '__main__':
    # path = "books/frankenstein.txt"

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # TODO : Add raise case for invalid path

    #print(getText(path))
    #print(countWords(path))
    #print(countChars(path))
    print(generateCharReport(path))
    #print(generateWordReport(path))