class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)

        for ti in range(n):
            for di in range(ti,n):
                if temperatures[ti] < temperatures[di]:
                    result.append(di-ti)
                    break

            else:
                result.append(0)

        return result