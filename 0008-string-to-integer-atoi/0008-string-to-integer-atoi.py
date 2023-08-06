import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', s)
        if not match:
            return 0

        result = int(match.group(1))
        result = max(min(result, 2**31 - 1), -2**31)
        return result