class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start, end = 0, 0
        n = len(fruits)
        ans1 = 0
        ans2 = 0
        ans = 0
        flag = 0
        temp1 = fruits[0]
        temp2 = fruits[0]
        while end < n :
            if fruits[end] != temp1 and fruits[end] != temp2 and temp1 != temp2: # 出现新数字的情况
                temp1 = temp2 # 第一个是之前的数字
                temp2 = fruits[end] # 第二个是当前的数字
                ans1 = ans2
                ans2 = 1
                temp_end = end # 当前位置
                while (fruits[temp_end] == temp1 or fruits[temp_end] == temp2) and temp_end >= start:# 符合替换后的就往前靠
                    temp_end -=1
                start = temp_end+1 # 开始位置在当前两个数字之前
            elif fruits[end] != temp1 and temp1 == temp2: # 和第一个数不一致且刚开始
                temp2 = fruits[end] # 那你是第二个数字
                ans2 += 1
            elif fruits[end] == temp1: # 第一个数字出现
                ans1 += 1
            elif fruits[end] == temp2: # 第二个数字出现
                ans2 += 1
            ans = max(ans,ans1 + ans2)
            if temp1 == fruits[end]: # 需要保持第二数字永远是最后一个出现的数字，与下一个衔接
                k = temp1
                temp1 = temp2
                temp2 = k
            end += 1
        return ans

# fruits = [1,2,1]
# fruits = [1,2,3,2,2]
# fruits = [3,3,3,1,2,1,1,2,3,3,4]
# fruits = [1,0,1,4,1,4,1,2,3] # temp2应当是留在最后的数字
# 俺不中嘞
fruits = [1,0,29,29,29,29,29,29,0,0,29,8,8,29,8,29,8,8,15,8,8,15,15,8,15,15,8,8,7,5]
print(Solution.totalFruit(Solution,fruits))
