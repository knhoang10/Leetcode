class Solution:
    def countSubstrings(self, s: str) -> int:
        'ababa'
        result = 0
        for i in range(len(s)):
            left = i
            right = i
            while left != -1 and right != len(s):
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
                    
            left = i
            right = i + 1
            while left != -1 and right != len(s):
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
        return result