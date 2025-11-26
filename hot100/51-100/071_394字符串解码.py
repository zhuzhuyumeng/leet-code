class Solution:
    def decodeString(self, s: str) -> str:
        num_stack  = []
        s_stack = []
        string = ""
        size = len(s)
        for i in range(size):# 遍历字符串，长数字如何加入呢
            if "0"<=s[i]<="9": #数字边界
                if i > 0 and "0"<=s[i-1]<="9":
                    num = num_stack.pop()
                    num_stack.append(num*10+int(s[i]))
                else:
                    num_stack.append(int(s[i]))
            elif s[i] == "[":
                s_stack.append(s[i])
            elif s[i] == "]":
                ttmp = ""
                tmp = ""
                num = num_stack.pop()
                while s_stack[-1]!="[":
                    tmp += s_stack.pop()
                for i in range(num):
                    ttmp += tmp
                s_stack.pop()
                s_stack.append(ttmp)# 处理好的加入进去
            else:
                s_stack.append(s[i])
        while s_stack:
            string += s_stack.pop()
        return string[::-1]

# 字符串如何处理分割啊，你非得纠结开头的有没有1，没有就是那个字符串啊
# 重复字符串怎放在已有字符串上
if __name__ == "__main__":
    # s = "31[a]2[bc]"
    s = "100[a2[bc]]"
    sol = Solution()
    print(sol.decodeString(s))