import sys

read = sys.stdin.readline

days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30,'December':31}

month = str(read())

print(days[month.strip()])
print(sorted(days))

day = list(days.values())
for y in range(len(day)):
    if day[y] == 31:
        key_list = list(days.keys())
        print(key_list[y], end=", ")

print()
days_sort = sorted(days.items(), key=(lambda x : x[1]),)
print(days_sort)

month = read().strip()
for m in days.keys():
    if m.startswith(month):
        print(days[m])
