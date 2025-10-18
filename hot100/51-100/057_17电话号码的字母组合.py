class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(depth,path):
            if depth >= size:# 如果数字都遍历过
                res.append(path)
                return
            ch = ord(digits[depth]) - ord("0") #当前字母的数字
            for i in range(len(phone[ch])):# 扫当前数字的字母，遍历path并添加，ch：位置0,1,2
                depth += 1
                dfs(depth, path+phone[ch][i])
                depth -= 1 # 记得回溯
            return


        if len(digits)==0:
            return 0
        phone = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        depth =0
        size = len(digits)
        path = ""
        dfs(depth,path)
        return res




if __name__ == '__main__':

    solution = Solution()
    res = solution.letterCombinations("23")
    print(res)