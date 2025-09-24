from collections import Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        cnt = Counter()
        left = 0
        ans = 0
        for right,x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt)>2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans,right-left+1)
        return ans
# 自己做一遍吧
# right是索引，x是索引位置的数字，cnt是Counter可以直接进行统计
# cnt统计的数字个数大于2，就要把原本最左边的那个数字消去，可能出现许多次
# 所以直接顺序将其减去，为0就结束了
fruits = [1,0,29,29,29,29,29,29,0,0,29,8,8,29,8,29,8,8,15,8,8,15,15,8,15,15,8,8,7,5]
print(Solution.totalFruit(Solution,fruits))
