class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lenzipped = len(set(zip(pattern, s.split())))
        lenpattern = len(set(pattern))
        lens = len(set(s.split()))
        
        return lenzipped == lenpattern == lens
        
solution = Solution()
print(solution.wordPattern("ab", "b c a"))