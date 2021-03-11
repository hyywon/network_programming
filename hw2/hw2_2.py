
def gcd(x, y):
    while y:
        x , y = y, x % y
    return x

A, B = input().split()
A = int(A) ; B = int(B)

print(gcd(A, B))