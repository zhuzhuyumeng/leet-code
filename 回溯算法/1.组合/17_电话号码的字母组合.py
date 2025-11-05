class Solution:
    def __init__(self):
        self.phone = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.res = []
        self.s = ""

    def letterCombinations(self, digits: str) -> list[str]:
        def backtracking(depth: int):
            if depth==size:
                self.res.append(self.s)
                return
            ch = ord(digits[depth])-ord("0")
            for i in range(len(self.phone[ch])):
                self.s += self.phone[ch][i]
                backtracking(depth+1)
                self.s = self.s[:-1]

        size = len(digits)
        depth = 0
        backtracking(depth)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    res = solution.letterCombinations("23")
    print(res)