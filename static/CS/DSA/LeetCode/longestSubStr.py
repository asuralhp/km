# start_temp +1 repeat
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        char_temp = s[0]
        start_temp = 0
        i = 1
        while i < len(s):
            if s[i] in char_temp:
                start_temp += 1
                i = start_temp
                char_temp = s[i]
            else:
                char_temp += s[i]
            longest = max(len(char_temp),longest)
            i += 1
        return longest
    
# range from left to right, left ++ til not in
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength