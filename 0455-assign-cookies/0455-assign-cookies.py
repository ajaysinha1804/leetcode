class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c_child=0
        cookies_index=0
        while cookies_index < len(s) and c_child < len(g):
            if s[cookies_index] >= g[c_child]:
                c_child +=1
            cookies_index +=1
        return c_child
        