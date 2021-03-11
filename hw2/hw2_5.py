
def num_list(num):
    for i in range(0,49):
        num.append(i)
    return num

def num2_list(num):
    for i in range(0,49):
        num.append(i**2)
    return num

num = []
num2 = []

print(num_list(num))
print(num2_list(num2))