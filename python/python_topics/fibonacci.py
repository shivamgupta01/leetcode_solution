# from functools import lru_cache
# memoitation = {}
# @lru_cache(maxsize=200)
def fib(n):

    # if n in memoitation:
    #     return memoitation[n]

    if n == 1:
        return  1
    elif n == 2:
        return   1
    elif n>2:
        return   fib(n-1) + fib(n-2)

    # memoitation[n] = result

print (fib(500))