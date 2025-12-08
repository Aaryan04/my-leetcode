class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curretH, curretM = map(int, current.split(':'))
        correctH, correctM = map(int, correct.split(':'))
        
        diff = (correctH * 60 + correctM) - curretH * 60 - curretM
        res = 0
        for v in [60, 15, 5, 1]:
            res += diff // v
            diff %= v
        return res