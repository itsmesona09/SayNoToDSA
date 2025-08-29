class Find_Anagrams:
    def findanagrams(self, s, p):
        arr = []
        for i in range(len(s)):
            arr.append(s[i : i + len(p)])
            
        val = []
        for i in range(len(arr)):
            if sorted(arr[i]) == sorted(p):
                val.append(i)
        return val

anagram = Find_Anagrams()
s = "cbaebabcd"
p = "abc"
print(anagram.findanagrams(s, p))