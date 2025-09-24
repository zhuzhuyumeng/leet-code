class Solution:
    def backspaceCompare(self,s: str, t: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch == "#":
                    ret.pop()
                else:
                    ret.append(ch)
            return "".join(ret)

        return build(s) == build(t)
# 列表当栈用
# 注意退格极限
# s = "ab#c"
# t = "ad#c"
# s = "ab##"
# t = "c#d#"
s = "xywrrmp"
t = "xywrrmu#p"
# s = "y#fo##f"
# t = "y#f#o##f"
print(Solution.backspaceCompare(Solution,s, t))
