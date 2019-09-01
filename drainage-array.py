def main():
    with open('map.txt') as f:
        numMaps = int(f.readline())
        for x in range(numMaps):
            line = f.readline()
            word = line.split()
            title = word[0]
            rows = int(word[1])
            cols = int(word[2])
            c = 0
            theMap = [[0 for x in range(cols)] for y in range(rows)]
            while c < rows:
                lineMap = f.readline()
                heights = lineMap.split()
                d = 0
                while d < cols:
                    theMap[c][d] = int(heights[d])
                    d = d + 1
                c = c + 1
            print title,":",findOverall(theMap, rows, cols)
             # printMap(theMap, rows, cols)

def findOverall (theMap, rows, cols):
    overall = 1
    lookUp = [[-1 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            lookUp[i][j] = findLongest(theMap, lookUp, rows, cols, i, j)
            if lookUp[i][j] > overall :
                overall = lookUp[i][j]
    return overall

def findLongest (theMap, lookUp, rows, cols, index1, index2):
    currentLong = 0
    if index1 > 0 and theMap[index1][index2] > theMap[index1 - 1][index2]:
        if lookUp[index1 - 1][index2] != -1 :
            if (currentLong < lookUp[index1 - 1][index2]) :
                currentLong = lookUp[index1 - 1][index2]
        else :
            recurse = findLongest(theMap, lookUp, rows, cols, index1 -1, index2)
            if (currentLong < recurse) :
                currentLong = recurse
    if index2 > 0 and theMap[index1][index2] > theMap[index1][index2 - 1]:
        if lookUp[index1][index2 - 1] != -1 :
            if (currentLong < lookUp[index1][index2 - 1]) :
                currentLong = lookUp[index1][index2 - 1]
        else :
            recurse = findLongest(theMap, lookUp, rows, cols, index1, index2  - 1)
            if (currentLong < recurse) :
                currentLong = recurse
    if index1 < (rows - 1) and theMap[index1][index2] > theMap[index1 + 1][index2]:
        if lookUp[index1 + 1][index2] != -1 :
            if (currentLong < lookUp[index1 + 1][index2]) :
                currentLong = lookUp[index1 + 1][index2]
        else :
            recurse = findLongest(theMap, lookUp, rows, cols, index1 + 1, index2)
            if (currentLong < recurse) :
                currentLong = recurse
    if index2 < (cols - 1) and theMap[index1][index2] > theMap[index1][index2 + 1]:
        if lookUp[index1][index2 + 1] != -1 :
            if (currentLong < lookUp[index1 ][index2 + 1]) :
                currentLong = lookUp[index1][index2 + 1]
        else :
            recurse = findLongest(theMap, lookUp, rows, cols, index1, index2 + 1)
            if (currentLong < recurse) :
                currentLong = recurse
    return currentLong + 1

def printMap(theMap, rows, cols) :
    for i in range(rows):
        for j in range(cols):
            print theMap[i][j], #
        print

if __name__ == '__main__':
    main()