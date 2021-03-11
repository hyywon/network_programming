
sum = []
num = []

def num_list(num):
    for i in range(1,1000):
        num.append(str(i))
    return num

def sum_list(num,sum):
    for j in num:
        count = 0
        for k in j:
            count += int(k)
        sum.append(count)
    return sum

num_list(num)
print(sum_list(num,sum))