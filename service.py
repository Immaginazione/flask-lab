def readData():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.read().split()
    except FileNotFoundError as error:
        print("file non trovato")
    return []

def showData(index):
    return readData()[index]

def createData(data):
    try:
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError as error:
        print("file non trovato")

def updateData(index, data):
    fileList = readData()
    fileList.insert(int(index), data)
    dataString = "\n".join(fileList)
    createData(dataString)


