class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()
        reverse_s = s[::-1]
        return " ".join(reverse_s)