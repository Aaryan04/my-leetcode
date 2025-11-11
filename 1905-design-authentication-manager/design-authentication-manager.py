class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tracker = {}     # id: expiry time
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tracker[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tracker:
            return
        if self.tracker[tokenId] > currentTime:
            self.tracker[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        expired_tokens = []
        for token_id, expiry_time in self.tracker.items():
            if expiry_time <= currentTime:
                expired_tokens.append(token_id)
            
        for token_id in expired_tokens:
            del self.tracker[token_id]

        return len(self.tracker)

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)