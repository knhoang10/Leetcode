class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         result = [];
#         arr = intervals[0]
#         i = 1
#         while i < len(intervals):
#             if arr[1] < intervals[i][0]:
#                 result.append(arr)
#                 arr = intervals[i]
            
#             if arr[1] >= intervals[i][0]:
#                 arr[1] = intervals[i][1]
                
#             if i == len(intervals) - 1:
#                 result.append(arr)
#             i += 1
#         if len(intervals) == 1:
#             result.append(arr)
#         return result

        intervals.sort(key = lambda i : i[0])
        output = [intervals [0]]
        for start, end in intervals [1:]:
            lastEnd = output [ - 1][1]
            if start <= lastEnd:
                output [-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output