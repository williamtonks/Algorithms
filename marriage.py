import math
import Queue
import sys
#William Tonks wrt6af I feel like I'm getting progressiely worse at coding

def main():
    with open('chapel.txt') as f:
        numVerts= int(f.readline())
        moveMap = [[sys.maxint for y in range(numVerts)] for x in range(numVerts)]
        ways = [[["", ""] for y in range(numVerts)] for x in range(numVerts)]
        luke = f.readline()
        lukey = luke.split()
        lukeStart = int(lukey[0])
        lukeEnd = int(lukey[1])
        lorel = f.readline()
        lorelkey = lorel.split()
        lorelStart = int(lorelkey[0])
        lorelEnd = int(lorelkey[1])
        edges = [[] for i in range(numVerts)]
        for x in range(numVerts):
            line = f.readline()
            edges[x].append(int(x))
            word = line.split()
            for y in word:
                edges[x].append(int(y))
                edges[int(y)].append(int(x))
        # for x in range(numVerts):
        #    for y in range(numVerts):
        #        if(x in edges[y] or x == y):
        #            moveMap[x][y] = -1
        finalWays = findMovesTo(moveMap, ways, edges, numVerts, lukeStart, lorelStart, lukeEnd, lorelEnd)
        print finalWays[0]
        print finalWays[1]

def findMovesTo(moveMap, ways, edges, numVerts, lukeStart, lorelStart, lukeEnd, lorelEnd):
    toVisit = Queue.Queue(maxsize = 0)
    toVisit.put([lukeStart, lorelStart])
    moveMap[lukeStart][lorelStart] = 0
    ways[lukeStart][lorelStart][0] = str(lukeStart)
    ways[lukeStart][lorelStart][1] = str(lorelStart)
    while toVisit.qsize() > 0:
        curState = toVisit.get()
        for x in edges[curState[0]]:
            for y in edges[curState[1]]:
                if(x not in edges[y] and not(x == y) and moveMap[x][y] > (moveMap[curState[0]][curState[1]] + 1)):
                    moveMap[x][y] = moveMap[curState[0]][curState[1]] + 1
                    ways[x][y][0] = ways[curState[0]][curState[1]][0] + " " + str(x)
                    ways[x][y][1] = ways[curState[0]][curState[1]][1] + " " + str(y)
                    toVisit.put([x, y])
    return ways[lukeEnd][lorelEnd]


if __name__ == '__main__':
    main()