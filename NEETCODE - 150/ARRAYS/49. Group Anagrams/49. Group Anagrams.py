class Anagram:
    def group_anagram(self, strs):
        hm = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in hm:
                hm[sorted_word].append(word)
            else:
                hm[sorted_word] = [word]

        return [v for k, v in hm.items()]
    
anagram = Anagram()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram.group_anagram(strs))
