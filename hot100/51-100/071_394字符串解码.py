class Solution:
    def decodeString(self, s: str) -> str:
        num_stack  = []
        string_stack = []
        size = len(s)
        for i in range(s):
            tmp = ""

# 字符串如何处理分割啊
if __name__ == "__main__":
    s = "3[a]2[bc]"
    sol = Solution()
    print(sol.decodeString(s))