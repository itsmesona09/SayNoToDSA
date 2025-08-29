class Permutation:
    def permutation(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1count = [0] * 26
        s2count = [0] * 26
        
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
            
        for i in range(len(s1), len(s2)):
            s2count[ord(s2[i]) - ord('a')] += 1
            s2count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if s1count == s2count:
                return True
        return False
        
permutate = Permutation()
s1 = "abc"
s2 = "eidbaooo"
print(permutate.permutation(s1, s2))