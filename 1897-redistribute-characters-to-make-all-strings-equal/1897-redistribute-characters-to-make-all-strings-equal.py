class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return not any([val % len(words) for val in collections.Counter("".join(words)).values()])
