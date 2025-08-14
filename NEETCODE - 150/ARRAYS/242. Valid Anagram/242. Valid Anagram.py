class Anagram:
    def valid_anagram(self, s, t):
        s, t = sorted(s), sorted(t)
        return s == t
        
anagram = Anagram()
s, t = "anagram", "nagaram"
# s, t = "anagramsk", "nagaram"
print(anagram.valid_anagram(s, t))