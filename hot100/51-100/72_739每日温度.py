from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0 for i in range(size)]
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res

        # size = len(temperatures)
        # res = [0 for i in range(size)]
        # stack = []
        # for i in range(size):
        #     if len(stack) == 0:
        #         stack.append(i)
        #     elif temperatures[i]>temperatures[stack[-1]]:
        #         while len(stack)>0 and temperatures[i]>temperatures[stack[-1]]:
        #             cur = stack.pop()
        #             res[cur] = i-cur
        #         stack.append(i)
        #     else:
        #         stack.append(i)
        # return list

# 维护单调栈，如果当前元素比栈顶元素大，栈顶元素出栈，直到没有，压入栈中
# 最后结束，站内元素出栈，全为0，初始化给0就不用再处理了

        #维护一个标记列表，每次都要给0的比较
        # size = len(temperatures)
        # res = []
        # for i in range(size):
        #     for j in range(i+1,size):
        #         if temperatures[j]>temperatures[i]:
        #             res.append(j-i)
        #             break
        #     if len(res)<i+1:
        #         res.append(0)
        # return res

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))
