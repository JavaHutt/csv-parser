import tablib

def main():
    imported_data = importFile('input.csv')
    parseCSV(imported_data)
    
def importFile(name):
    fh = open(name, 'r')
    return tablib.Dataset().load(fh)

def parseCSV(data):
    print(data[0])
    print(data[1][0])
    print(data['request.app.bundle'][0])

main()