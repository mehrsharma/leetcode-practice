class solution:
    def longestSubstring(s: str) -> int:
        length = 0
        left = 0
        right = 0
        chars = []
        for i in range (0, len(s)):
            if s[i] not in chars:
                right = i
                chars.append(s[i])
                length = max(length, right - left + 1)
            else:
                chars.append(s[i])
                right = i
                while len(chars) != len(set(chars)):
                    chars.pop(0)
                    left += 1
        return length
# slow, optimize while loop
