#-----------Excercise 1-----------
def readFile():
    fileName = input("Please enter the file name: ")
    try:
        fileHandler = open(fileName, "r")
        content = fileHandler.read()
        fileHandler.close()
        print(content)
    except:
        print("File not found")

#-----------Excercise 2-----------
def writeFile():
    fileName = input("Please enter the file name: ")
    fileHandler = open(fileName, "w")
    content = input()
    fileHandler.write(content)
    fileHandler.close()
    print(content)
    
#readFile()
writeFile()