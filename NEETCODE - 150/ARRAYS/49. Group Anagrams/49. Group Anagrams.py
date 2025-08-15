from collections import defaultdict
class Anagram:
    # def group_anagram(self, strs):
    #     hm = {}
    #     for word in strs:
    #         sorted_word = "".join(sorted(word))

    #         if sorted_word in hm:
    #             hm[sorted_word].append(word)
    #         else:
    #             hm[sorted_word] = [word]

    #     return [v for k, v in hm.items()]
    
    # or
    
    def group_anagram(self, strs):
        hm = defaultdict(list) #create a list dictionary
        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1
            # dictionary in Python is hashable [contents cannot be changed]
            # list in Python is unhashable(mutable) [contents can be changed]
            # the keys must be hashable, but the values need not be hashable
            # so we use tuple which is hashable, for the count key
            #                                           key                                 :         value                                        
            # (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate']
            hm[tuple(count)].append(word)
        return [v for k, v in hm.items()]
    
anagram = Anagram()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram.group_anagram(strs))
