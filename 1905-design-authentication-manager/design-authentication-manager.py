class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tracker = defaultdict(int)      # id: expiry time
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tracker[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tracker[tokenId] > currentTime:
            self.tracker[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for token in self.tracker:
            if self.tracker[token] > currentTime:
                cnt += 1
        return cnt

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)