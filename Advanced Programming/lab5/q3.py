class Subsets:
    def __init__(self, arr):
        self.arr = arr
    
    def uniquesubsets(self, idx, subset, result):
        if (len(subset) != 0):
            if (subset not in result):
                result.append(subset[:])
 
        for j in range(idx, len(self.arr)):
       
            subset.append(self.arr[j])
            self.uniquesubsets(j + 1, subset, result)
 
            subset.pop()
    
    def getsubsets(self):

        subsets = []
        result = []

        self.uniquesubsets(0, subsets, result)

        res = []
        for i in result:
            res.append(list(i))

        return res

arr = input("Enter a list of numbers: ").split()
A = Subsets(arr)

result = A.getsubsets()

for i in range(len(result)):
    temp = result[i]
    for j in range(len(temp)):
        print(temp[j], end=" ")
    print()