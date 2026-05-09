import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        edges = collections.defaultdict(list) # 创建了一个默认值为列表的字典
        indeg = [0]*numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])# 当前节点的后置节点，学习info[0]之前要先学info[1],info[0]的出节点
            indeg[info[0]] += 1 # 这个是info[0]入度
        # 找到入度为0的节点
        q = collections.deque(u for u in range(numCourses) if indeg[u]==0)
        visited = 0
        # 标记访问过的入度为0节点

        while q:
            visited += 1
            u = q.popleft()
            # 该节点的后置节点入度-1，消除本节点的影响
            for v in edges[u]:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
        return visited == numCourses

if __name__ == "__main__":
    # prerequisites = [[1,0]]
    # numCourses =
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # numCourses = 2
    # prerequisites = [[1,0],[0,1]]
    print(Solution.canFinish(Solution,4,prerequisites))

"""
拓扑排序，入度出度
入度如何保存，入的边，入度数量
入度为0入队，遍历其出度
"""