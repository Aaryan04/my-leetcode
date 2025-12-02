class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}        # {(1,1): ['ab', 'cd']}

        for s in strings:
            key_list = []
            for i in range(len(s) - 1):
                diff = (ord(s[i+1]) - ord(s[i]) + 26) % 26   # circular difference = next - curr + 26
                key_list.append(diff)

            key = tuple(key_list)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        return list(hashmap.values())
            

