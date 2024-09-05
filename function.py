def cal_sum(a,b):
    return a+b

print(cal_sum(2,4))


def pri():
    print("hello world")

pri()


def avg(a,b,c):
    return (a+b+c)/3

ans=avg(23,43,4)

print(ans)


#   default argument :-------


def mul(a=1,b=1):
    return a*b

mul()
print(mul())