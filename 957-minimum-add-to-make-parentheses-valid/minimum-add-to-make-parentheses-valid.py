class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_br = []
        close_br = 0

        for br in s:
            if br == '(':
                open_br.append(br)
            elif br == ')' and open_br:
                open_br.pop()
            else:
                close_br += 1

        return len(open_br) + close_br
