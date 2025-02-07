
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
    report += f"{countWords(path_to_file)} words found in file.\n\n"
    
    for sChar in sortedChars:
        if sChar.isalpha():
            report += f"The '{sChar}' char was found {chars[sChar]} times.\n"
    report += f"\n--- End Report ---"
    
    return report


if __name__ == '__main__':
    path = "books/frankenstein.txt"

    #print(getText(path))
    #print(countWords(path))
    #print(countChars(path))
    print(generateCharReport(path))