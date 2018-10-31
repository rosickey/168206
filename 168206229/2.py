#斐波那切数列 尾递归
def fibo(first, second, n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return first+second
    else:
        return fibo(second, first+second, n-1)

for i in range(1,20):
    print(fibo(1, 1, i))
