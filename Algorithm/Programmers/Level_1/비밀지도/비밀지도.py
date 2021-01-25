n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def change_binary(x,n):
    binary = [0 for _ in range(n)]
    count = n-1
    while (x!=0):
        if x%2 == 1:
            binary[count]="#"
        elif x%2 == 0:
            binary[count]=" "
        x//=2
        count -= 1 
    return binary

def solution(n,arr1,arr2):
    newGraph = []
    for i in range(n):
        newArr1 = change_binary(arr1[i],n)
        newArr2 = change_binary(arr2[i],n)
        new = []
        for a,b in zip(newArr1,newArr2):
            if a=="#" or b=="#":
                new.append("#")
            else:
                new.append(" ")
        newGraph.append("".join(new))
    return newGraph

print(solution(n,arr1,arr2))

print(str(bin(arr1[0]|arr2[0])[2:]).replace("1","#").replace("0"," "))

