class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Have a maximum 
        maxOne = 0
        
        count = 0
        for i in range(len(nums)):
            # Start counting until you reach to 0
            if nums[i] == 1:
                count += 1

            # Check if max is less than count then max equal count and reset count
            else:
                if maxOne < count:
                    maxOne = count

                count = 0
        
        return max(count, maxOne)
        