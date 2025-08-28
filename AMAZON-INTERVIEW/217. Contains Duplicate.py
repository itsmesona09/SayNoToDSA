class Contains_Duplicate:
    def contain_dupl(self, arr):
        return len(set(arr)) != len(arr)
        
dup = Contains_Duplicate()
arr = [1, 2, 3, 1]
print(dup.contain_dupl(arr))