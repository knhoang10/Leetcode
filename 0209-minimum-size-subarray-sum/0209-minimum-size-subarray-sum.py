class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Have a left pointer and result to equal to the length of the list + 1
        # Loop through the list until the sum is greater than or equal to target
        # If the sum is greater than the target, start subtracting from the left side until it's less than the target
        # Get the minimum of the result and length of the window 
        left = 0
        result = len(nums) + 1
        totalSum = 0
        resultExist = False
        for right in range(len(nums)):
            totalSum += nums[right]
            while totalSum >= target:
                result = min(result, right-left+1)
                totalSum -= nums[left]
                left += 1
                resultExist = True
            
        
        if resultExist:
            return result
        else:
            return 0