def fact(num):
    if num==0:
        return 1
    s = num * fact(num-1)
    return s

num = 5
print(fact(num))
