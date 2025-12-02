from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        for num in nums:
            counter_map[num] = counter_map.get(num,0)+1 #出现过，原来次数+1；没出现过，0+1
            print(counter_map[num])
        heap = []

        def swap(i:int,j:int):
            heap[i], heap[j] = heap[j], heap[i]

        def sift_up(index): # 把大数换下来
            while index>0:
                parent = (index-1)//2 # 小一点、/2向下取整
                if heap[parent][0]>heap[index][0]:
                    swap(parent,index)
                    index = parent
                else:
                    break

        def sift_down(index):
            n = len(heap)
            while 2*index+1<n:
                child = 2 * index +1
                if child + 1 < n and heap[child+1][0]<heap[child][0]: #如果有右子节点，因为小根堆的右边应该是更大的。错误的没关系，只找两边哪个更小
                    child += 1
                if heap[child][0]<heap[index][0]:
                    swap(child, index)
                    index = child
                else:
                    break

        def heap_push(item):
            heap.append(item)
            sift_up(len(heap)-1) # 从尾上浮

        def root_replace(item):
            heap[0] = item
            sift_down(0) # 从顶下沉

        for num , freq in counter_map.items():
            item = (freq,num)
            if len(heap)<k:
                heap_push(item)
            else:
                if freq<heap[0][0]:
                    continue
                elif freq>heap[0][0]:
                    root_replace(item)

        return [item[1] for item in heap]



# 来一个建堆操作，新元素加到末尾，再上浮新元素到数组合适位置
# 小顶堆，频率少的在上面，但是大一点就可以把它取代，是找大数的


        # count_dict = {}
        # for num in nums:
        #     if num not in count_dict:
        #         count_dict[num] = 1
        #     else:
        #         count_dict[num] += 1
        # # 用count_dict里面的元素，排序数字是第二个元素，降序
        # sorted_items = sorted(count_dict.items(),key=lambda x: x[1],reverse=True)
        # res = []
        # for i in range(k):
        #     res.append(sorted_items[i][0])
        # return res

# 我的想法是一个数组存放所有元素，然后排序数组
if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]
    # k = 2
    # nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    nums =[5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3]
    k = 3
    sol = Solution()
    print(sol.topKFrequent(nums,k))