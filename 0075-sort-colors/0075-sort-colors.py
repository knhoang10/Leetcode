class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         # Count how many 0, 1, 2
#         # Loop through 0, 1, 2 and replace numbers in num
#         numsDict = {
#             0:0,
#             1:0,
#             2:0
#         }
#         for i in range(len(nums)):
#             numsDict[nums[i]] += 1
        
#         result = [0] * numsDict[0] + [1] * numsDict[1] + [2] * numsDict[2]

#         for i in range(len(nums)):
#             nums[i] = result[i]
            
        def switch(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
            
        # Two pointer
        left = 0
        right = len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                switch(left, i)
                left += 1
            elif nums[i] == 2:
                switch(right, i)
                right -= 1
                i -= 1
            i += 1
        