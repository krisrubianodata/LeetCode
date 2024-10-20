class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        first = 0
        last = len(s) - 1

        while first < last:
            if s[first] not in vowels:
                first += 1
            elif s[last] not in vowels:
                last -= 1
            else:
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1
                
        return "".join(s)