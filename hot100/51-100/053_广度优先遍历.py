import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        edges = collections.defaultdict(list) # 每个课程的出
        indeg = [0]*numCourses # 每个课程的入度

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]]+=1

        deque = collections.deque()
        for i in range(numCourses):
            if indeg[i] ==0:
                deque.append(i)
        visited = 0
        while deque:
            visited += 1
            cur = deque.popleft()
            for v in edges[cur]:
                indeg[v]-=1
                if indeg[v] == 0:
                    deque.append(v)
        return visited == numCourses


prerequisites = [[0,1]]
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 2
# prerequisites = [[1,0],[0,1]]
print(Solution.canFinish(Solution,numCourses,prerequisites))
