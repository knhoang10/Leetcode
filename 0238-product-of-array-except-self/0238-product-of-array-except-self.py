class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre = []
        post = []
        for i in range(len(nums)):
            try:
                pre.append(pre[-1] * nums[i])
            except:
                pre.append(nums[i])
        for i in range(len(nums) - 1, -1, -1):
            try:
                post.insert(0, post[0] * nums[i])
            except:
                post.insert(0, nums[i])
        for i in range(len(nums)):
            if i - 1 == - 1:
                result.append(post[i+1])
            elif i + 1 == len(nums):
                result.append(pre[i-1])
            else:
                result.append(pre[i-1] * post[i+1])
        return result