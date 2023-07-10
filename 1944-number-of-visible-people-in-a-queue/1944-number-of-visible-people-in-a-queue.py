class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
#         stack = []
#         result = []
#         resultExist = False
#         for i in range(len(heights)-1, -1, -1):
#             count = 0
#             for k in range(len(stack)-1, -1, -1):
#                 if heights[i] > heights[stack[k]]:
#                     count += 1
#                 else:
#                     count += 1
#                     break
#             result.insert(0, count)

                
#             for j in range(len(stack)-1, -1, -1):
#                 if heights[i] < heights[stack[j]]:
#                     stack.append(i)
#                     resultExist = True
#                     break
#                 else:
#                     stack.pop(len(stack)-1)
                    
#             if resultExist == False:
#                 stack.append(i)
#             else:
#                 resultExist = False
            
                
#         return result

        stack = []
        result = [0] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                count += 1
                stack.pop()
                
            if stack:
                count += 1
                
            result[i] = count
            stack.append(heights[i])
        
        return result