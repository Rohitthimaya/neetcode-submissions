class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        j = len(s1) - 1
        for i in range(len(s2)):
            s2Counter = Counter(s2[i:j + 1])
            print(s2Counter)
            if(s1Counter == s2Counter): return True
            j += 1
        return False