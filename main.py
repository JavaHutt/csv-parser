import tablib
import json

urlPrefix = 'https://appgallery.cloud.huawei.com/ag/n/app/C27162'

def main():
    importedCsv = importTable('input.csv')
    importedJSON = open('map.json', 'r')
    importedMap = json.load(importedJSON)
    csvDict = CSVtoDict(importedCsv)
    concatinated = concatinateDicts(importedMap, csvDict)
    jsonDump = json.dumps(concatinated)
    jsonFile = open("output.json", "w")
    jsonFile.write(jsonDump)
    jsonFile.close()

def concatinateDicts(target, source):
    result = target.copy()

    for bundle, url in source.items():
        url = url.strip()
        if url == '':
            result.pop(bundle, None)
            continue
        if bundle not in result:
            result[bundle] = createURL(urlPrefix, url)
            continue
        result[bundle] = createURL(result[bundle], url)
        

    return result

def createURL(oldURL, newURL):
    oldURLWithoutID = oldURL[:oldURL.rindex('/')]
    newID = newURL[newURL.rindex('/'):]
    return oldURLWithoutID + newID

def importTable(name):
    fh = open(name, 'r')
    return tablib.Dataset().load(fh)

def CSVtoDict(data):
    d = dict()
    for row in data:
        bundle, url = row[1], row[4]
        d[bundle] = url
    return d

main()