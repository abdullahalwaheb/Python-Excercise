import io

def word_histogram():
    wordSummary = {}
    text = io.StringIO(input('please enter a text: '))
        
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

word_histogram()