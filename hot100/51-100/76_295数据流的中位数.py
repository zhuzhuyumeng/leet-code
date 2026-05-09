import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num) #走一遍放小数的堆
        max_of_small = - heapq.heappop(self.small) #取出小堆的最大数

        heapq.heappush(self.large,max_of_small) # 给大堆

        if len(self.small)< len(self.large): #大堆比小堆长，还给小堆
            min_of_large = heapq.heappop(self.large)
            heapq.heappush(self.small,-min_of_large)



    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0]+self.large[0])/2


# 如果这个就是一个堆，放进去就排好序了。错啦，堆只对上下节点排序，不对左右节点排序
# 直接分成大小堆，那我怎么知道哪个数放哪个位置捏
# 大顶堆放小数，因为堆顶是小数中的最大值，小顶堆放大数，堆顶是其中最小的数，就有了中间的两边数
# 整个过程就是所有数字先进一遍小池子，小池子自动把最大的浮出来，然后把浮出来的丢给右边，小顶堆只放大数
# 右边池子多于左边，就要把堆顶的还给左边。
# 只在计算的时候看一下长度
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())