def letter_histogram():
    letterSummary = {}
    word = input("word? ")

    for i in word:
        counter = 0
        for j in word:
            if i == j:
                counter += 1
                letterSummary[i] = counter
    
    print(letterSummary)

letter_histogram()