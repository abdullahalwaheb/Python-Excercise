import json
from matplotlib import pyplot

dataList = []

def readData():
    fileHandler = open('data.json', 'r')
    data = json.load(fileHandler)
    print(data)
    for i in data:
        dataList.append(data)
    fileHandler.close()
    print(dataList)

def run():
    ys = []
    for x in dataList:
        ys.append(x)
    pyplot.plot(dataList, ys)
    pyplot.show()

if __name__ == "__main__":
    readData()
    #run()



