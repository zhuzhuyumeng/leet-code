class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        path = ""
        def dfs(start:int,path):
            if start ==n:
                res.append(path)
                return
            index = ord(digits[start])-ord('0')
            for i in range(len(phone[index])): # 当前字母的每个字符
                dfs(start+1,path+phone[index][i])

        phone = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        dfs(0,path)
        return res


if __name__ == '__main__':

    solution = Solution()
    res = solution.letterCombinations("23")
    print(res)