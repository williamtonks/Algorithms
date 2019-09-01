def getShit():
    points = []
    with open('garden.txt') as f:
        num_points = int(f.readline())
        data = f.readlines()
        for line in data:
            word = line.split()
            word = list(map(float, word))
            points.append(word)
    # print(points)
    return points

def brute(points) :
    closestPoints = []
    i = 0
    # delta = 1000000 define delta to be largest of whatever you need
    while i < len(points) :
        temp = i + 1
        while temp < len(points) :
            capture = dist(points[i], points[temp])
            if capture < delta :
                delta = capture
            temp = temp + 1
        i = i + 1
    print(delta)

def dist(point1, point2):
    return ((point2[0] -point1[0])**2 + (point2[1] -point1[1])**2)**.5

def recurseDown(points):
    if len(points) == 1:
        return points[:], points[:]
    if len(points) == 2:
        if(points[1][1] < points[0][1]):
            return points[:], [points[1], points[0]]
        return points[:], [points[0], points[1]]
    length = len(points)//2
    left = points[:length]
    right = points[length:]
    closestPoints = []
    closestLeft, leftSideY = recurseDown(left)
    closestRight, rightSideY = recurseDown(right)
    if len(closestLeft) == 1 :
        closest = closestRight
    elif len(closestRight) == 1 :
        closest = closestLeft
    else :
        if dist(closestLeft[0], closestLeft[1]) > dist(closestRight[0], closestRight[1]):
            closest= closestRight
        else :
            closest = closestLeft
    delta = dist(closest[0], closest[1])
    median = (left[-1][0] + right[0][0])/2
    # Merge by Y order
    sortedList = merge(leftSideY, rightSideY)
    # Build a list of points in the runway, sorted by y-order
    inDelta = []
    for element in sortedList :
        if (abs(median - element[0])) < delta:
            inDelta.append(element)
    i = 0
    # for each point in the runway, check dist between that and the next 15 points in delta, store points that give lowest dist
    # take the minimum of those distances and delta, pass on the set of points that give lowest plus Y sortedlist
    while i < len(inDelta):
        temp = 1
        while temp < 15 and (i+temp) != len(inDelta) :
            if  delta > dist(inDelta[i], inDelta[i+temp ]) :
                delta = dist(inDelta[i], inDelta[i+temp ])
                closest = [inDelta[i], inDelta[i+temp]]
            temp = temp + 1
        i = i + 1
    return closest, sortedList

def merge(leftSide, rightSide):
    sortedY = []
    while len(leftSide) > 0 and len(rightSide) > 0 :
        if(leftSide[0][1] < rightSide[0][1]):
            sortedY.append(leftSide[0])
            del leftSide[0]
        else:
            sortedY.append(rightSide[0])
            del rightSide[0]
    if len(leftSide) == 0 :
        for element in rightSide :
            sortedY.append(element)
    else:
        for element in leftSide :
            sortedY.append(element)
    return(sortedY)

def main():
    points = getShit()
    list.sort(points)
    # brute(points)
    finalPoints, sortedY = recurseDown(points)
    print (dist(finalPoints[0], finalPoints[1]))

if __name__ == '__main__':
    main()