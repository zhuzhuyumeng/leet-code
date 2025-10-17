import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def dfs(cur: int):
            nonlocal valid
            # 当前点在搜索
            visited[cur] = 1
            # 扫图
            for v in edges[cur]:
                # 扫到自己，不符合
                if visited[v] == 1:
                    valid = False
                    return
                # 这个点没有扫过，深度扫
                elif visited[v] == 0:
                    dfs(v)
            visited[cur] = 2 # 标记为扫过
            result.append(cur)
            return
        visited = [0]*numCourses
        result = list()
        valid = True
        edges = collections.defaultdict(list)
        # 添加边图
        for info in prerequisites:
            edges[info[1]].append(info[0]) # 后一个是前面一个的前置条件
        for i in range(numCourses):
            if valid and visited[i] == 0: # 扫图。无环，未搜索过
                dfs(i)

        return valid


# prerequisites = [[1,0]]
# numCourses =
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# numCourses = 2
# prerequisites = [[1,0],[0,1]]
print(Solution.canFinish(Solution,4,prerequisites))

"""
都扫一遍然后不能有互相抵达的课程，拓扑排序
如何表示这个

"""