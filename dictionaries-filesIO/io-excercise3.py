import io
#a method to count letters
def letter_histogram(content):
    letterSummary = {}
    for i in content:
        counter = 0
        for j in content:
            if i == j:
                counter += 1
                letterSummary[i] = counter
    print(letterSummary)

#a method to count words
def word_histogram(content):
    wordSummary = {}
    text = io.StringIO(content)

    for string in text:
        word = string.split()
        myTuple = (word)

    for i in myTuple:
        counter = 0
        wordSummary[i] = counter
        for j in myTuple:
            if i == j:
                counter += 1
                wordSummary[i] = counter
    print(wordSummary)

#a method to read the file content
def readFile():
    fileName = input("Please enter the file name: ")
    try:
        fileHandler = open(fileName, "r")
        content = fileHandler.read()
        #calling the letters counting method
        letter_histogram(content)
        #calling the words counting method
        word_histogram(content)
        fileHandler.close()
    except:
        print("File not found")

readFile()