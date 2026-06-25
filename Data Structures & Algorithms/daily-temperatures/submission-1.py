class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []


        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tt, ii = stack.pop()
                result[ii] = (i - ii)

            stack.append([t,i])            

        return result