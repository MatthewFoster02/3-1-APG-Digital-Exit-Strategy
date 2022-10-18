# Basic data model to read in the data, first attempt
rows = []
data_dict = {}

def readIn():
    data = ""
    with open("data/testdata.csv", "r") as file:
        data = file.read()
    return data

def parseData(data):
    dataRows = data.split("\n")
    i = 0
    for row in dataRows:
        if i == 0:
            global headers 
            headers = row.split(",")
        elif i < len(dataRows)-1:
            rows.append(row.split(","))
        i += 1

def construct_dict():
    for header in headers:
        data_dict[header] = []
    for row in rows:
        i = 0
        for header in headers:
            data_dict[header].append(row[i])
            i += 1

parseData(readIn())
construct_dict()
print(f"Dictionary: {data_dict}")
