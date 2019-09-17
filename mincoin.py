#code
def ex(num):
    numOfCoins = []
    if num == 0:
        return 0
    for i in range(len(currency)):
        temp = currency[i]
        if num >= temp:
            if minCoin[num - temp] != -1 :
                numOfCoins.append(minCoin[num - temp] + 1)
            else:
                numOfCoins.append(ex(num - temp) + 1)
    numOfCoins.sort()
    minCoin[num] = numOfCoins[-1]
    print("Minimum for" + str(num) + "is" + str(minCoin[num]))
    return numOfCoins[-1]
    
cases = int(input("Enter the number of test cases \n"))
minCoin = []
currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
for i in range(cases):
    num = int(input("Enter a number for which minimum #coin change. \n"))
    minCoin = [-1]*num
    charlie = ex(num)
    print(charlie)