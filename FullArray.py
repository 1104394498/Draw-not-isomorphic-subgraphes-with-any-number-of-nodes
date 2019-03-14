import copy

visit = None
fullArrays = None

def getFullArray(num, startNO):
    global visit, fullArrays
    fullArrays = []
    visit = [False]*num
    subFullArray([],num, startNO)
    return fullArrays

def subFullArray(curArray, num, startNO):
    global visit
    if len(curArray) == num:
        fullArrays.append(curArray)
        return
    
    for i in range(num):
        if not visit[i]:
            visit[i] = True
            newArray = copy.deepcopy(curArray)
            newArray.append(startNO + i)
            subFullArray(newArray, num, startNO)
            visit[i] = False
            
if __name__ == '__main__':
    getFullArray(4,2)