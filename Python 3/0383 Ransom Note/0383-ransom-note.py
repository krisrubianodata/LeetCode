from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)

        for c in magazine:
            counter[c] += 1