class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        lmax = 0
        rmax = 0
        llist = []
        rlist = []
        count = 0
        for i in range(n):
            lmax = max(height[i],lmax)
            llist.append(lmax)
        for i in range(n-1,-1,-1):
            rmax = max(height[i],rmax)
            rlist.append(rmax)
        rlist.reverse()
        for i in range(n):
            sum = min(llist[i],rlist[i])-height[i]
            count = count + sum
        # print(llist)
        # print(rlist)
        return count


# 两个数组，维护左边最大以及右边最大
height =[0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution.trap(Solution,height))