from audioop import reverse


class Solution:
    def rotate(self, nums:list[int], k:int) -> None:
        n = len(nums)
        true_k = k%n
        tmp = nums[n-true_k:n]
        for i in range(n-1,true_k-1,-1):
            nums[i] = nums[i-true_k]
        nums[0:true_k] = tmp
        print(nums)

    def rotate2(self, nums:list[int], k:int) -> None:
        if not nums:
            return
        n = len(nums)
        true_k = k%n
        nums.reverse()
        nums[:true_k] = reversed(nums[:true_k]) # 反向迭代器，类似于赋值过去
        nums[true_k:n] = reversed(nums[true_k:n])

        # nums[0:true_k].reverse() #这样子是切出一个新列表
        # nums[true_k:n].reverse()



"""
如果轮转的字符比字符串长度多，取模运算，找到真实的轮转次数
向右轮转，倒着找到k个数字取出来
三次翻转，全部翻转，前k个翻转，剩下n-k个翻转
"""
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    # nums = [1,2]
    # k = 7
    print(Solution.rotate2(Solution,nums,k))