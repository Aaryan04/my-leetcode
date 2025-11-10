class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # my approach => complex and repititive
        # index = defaultdict(list)
        # for i, word in enumerate(wordsDict):
        #     index[word].append(i)

        # min_diff = float("inf")

        # if word1 == word2:
        #     lst = index[word1]
        #     for i in range(len(lst) - 1):
        #         min_diff = min(min_diff, lst[i+1] - lst[i])
        #     return min_diff

        # lst1, lst2 = index[word1], index[word2]
        # l1, l2 = 0, 0 

        # while l1 < len(lst1) and l2 < len(lst2):
        #     min_diff = min(min_diff, abs(lst1[l1] - lst2[l2]))
        #     if lst1[l1] < lst2[l2]:
        #         l1 += 1
        #     else:
        #         l2 += 1 

        # return min_diff

        # Optimized one pass approach

        min_diff = float('inf')
        i1 = -1
        i2 = -1

        for i, word in enumerate(wordsDict):
            
            if word == word1:
                i1 = i
            
            if word == word2:
                if word1 == word2:
                    i1 = i2
                i2 = i
        
            if i1 != -1 and i2 != -1:
                min_diff = min(min_diff, abs(i1 - i2))
            
        return min_diff