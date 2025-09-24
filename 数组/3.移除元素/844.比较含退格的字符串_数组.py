class Solution:
    def backspaceCompare(self,s: str, t: str) -> bool:
        s_low, s_fast = 0, 0
        s_len = len(s)
        s_array = [0 for _ in range(s_len)]
        while s_fast < s_len:
            s_array[s_low] = s[s_fast]
            s_low += 1 # 赋值结束就得把他加上去，留到判断结束会有少-1的情况，因为有归零操作
            if s[s_fast] == '#':
                s_low -= 2
                if s_low < 0:
                    s_low = 0
            s_fast += 1
        t_low, t_fast = 0, 0
        t_len = len(t)
        t_array = [0 for _ in range(t_len)]
        while t_fast < t_len:
            t_array[t_low] = t[t_fast]
            t_low += 1
            if t[t_fast] == '#':
                t_low -= 2
                if t_low < 0:
                    t_low = 0
            t_fast += 1
        if (s_low == t_low) and s_low<=0: #都退没了，全空
            return True
        if s_low == t_low: # 字符串存在，一一判断是否相同
            for i in range(0,min(s_low,t_low)):
                if s_array[i] != t_array[i]:
                    return False
        else: # 退格后的数组长度不相同，包不相同
            return False
        return True

# 注意退格极限
# s = "ab#c"
# t = "ad#c"
s = "ab##"
t = "c#d#"
# s = "xywrrmp"
# t = "xywrrmu#p"
# s = "y#fo##f"
# t = "y#f#o##f"
print(Solution.backspaceCompare(Solution,s, t))
