# Basic data model to read in the data, first attempt
rows = []

def readIn():
    data = ""
    with open("data/testdata.csv", "r") as file:
        data = file.read()
    return data

def parseData(data):
    data = data.replace("\n", ",")
    data = data.split(",")
    return data

data = parseData(readIn())
print(data)
