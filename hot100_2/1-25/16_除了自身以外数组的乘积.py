class Solution:
    def productExceptSelfPro(self, nums:list[int]) -> None:
        n = len(nums)
        left = [1]*n
        right = [1]*n

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1] # 轮不到最后一个数字算前缀和
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(n):
            nums[i] = left[i]*right[i]
        return nums

    def productExceptSelf(self, nums:list[int]) -> None:
        n = len(nums)
        left = [1]*(n+1)
        right = [1]*(n+1)

        for i in range(n):
            left[i+1] = left[i]*nums[i]
        for i in range(n-1,-1,-1):
            right[i] = right[i+1]*nums[i]
        left.pop(-1)
        right.pop(0)
        for i in range(n):
            nums[i] = left[i]*right[i]
        print(left)
        print(right)
        print(nums)
        return nums


"""
前后缀积，左右开弓，太聪明了，一个数字的积就是前缀积*后缀积
"""
if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(Solution.productExceptSelfPro(Solution,nums))