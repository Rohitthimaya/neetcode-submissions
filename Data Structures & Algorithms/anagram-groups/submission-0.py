class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = {}
        res = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in resDict:
                arr = resDict[sortedWord].append(word)
            else:
                resDict[sortedWord] = [word]
        
        for key in resDict:
            res.append(resDict[key])

        return res