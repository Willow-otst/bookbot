
def printText():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def countWords():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        print(len(file_contents.split()))

if __name__ == '__main__':
    #printText()
    countWords()