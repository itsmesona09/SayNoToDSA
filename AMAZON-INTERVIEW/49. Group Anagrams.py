from collections import defaultdict

class Group_Anagrams:
    def group_anagrams(self, strs):
        # hm = {}
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     if key not in hm:
        #         hm[key] = []
        #     hm[key].append(s)
            
        # return list(hm.values())
        
        hm = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hm[tuple(count)].append(s)
            
        return list(hm.values())
        
anagram = Group_Anagrams()
strs = ["eat","tea","tan","ate","nat","bat"]
print(anagram.group_anagrams(strs))