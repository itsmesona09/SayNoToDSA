class Valid_Anagram:
    def anagram(self, s, t):
        # return sorted(s) == sorted(t)
        hms, hmt = {}, {}
        for i in range(len(s)):
            hms[s[i]] = hms.get(s[i], 0) + 1
            hmt[t[i]] = hmt.get(t[i], 0) + 1
        
        return hms == hmt
    
valid_anagram = Valid_Anagram()
s, t = "anagram", "nagaram"
print(valid_anagram.anagram(s, t))