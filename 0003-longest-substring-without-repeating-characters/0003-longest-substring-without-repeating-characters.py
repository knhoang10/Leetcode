class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window technique - 2 pointer technique
        # Create a left pointer that starts at 0
        # Create an empty set
        # Create a max length number that starts at 0
        # Have a right pointer that loops through the string
        # If there is no repeating characters, keep adding - move the right pointer right
        # If there is a repeating character, subtract move the left pointer right and keep continuing until the character does not exist in the set
        # Check if the length of the window is greater than the max length number
        
        left = result = 0
        nonRepeatingCharacterSet = set()
        for right in range(len(s)):
            if s[right] not in nonRepeatingCharacterSet:
                nonRepeatingCharacterSet.add(s[right])
            else:
                while s[right] in nonRepeatingCharacterSet:
                    nonRepeatingCharacterSet.remove(s[left])
                    left += 1
                nonRepeatingCharacterSet.add(s[right])
            
            result = max(result, right-left+1)
            
        return result