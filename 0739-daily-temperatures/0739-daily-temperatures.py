class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        tempExist = False
        for i in range(len(temperatures)-1, -1, -1):
            for j in range(len(stack)-1, -1, -1):
                if temperatures[i] < temperatures[stack[j]]:
                    stack.append(i)
                    tempExist = True
                    result.insert(0, stack[j]-i)
                    break
                else:
                    stack.pop(len(stack) - 1)
                    
            if tempExist == False:
                result.insert(0, 0)
                stack.append(i)
            else:
                tempExist = False
        
        return result