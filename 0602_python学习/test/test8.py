#求大于n的最小整数
n = input()
n = eval(n)
mid_num = int(n)
if mid_num > n:
    min_int = mid_num
if mid_num <= n:
    min_int = mid_num +1
print(min_int)
