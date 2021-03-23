import sys
read = sys.stdin.readline

d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''}, {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

def num1():
    for p in d:
        val = p.values()
        val_list = list(val)
        name, phone, email = val_list
        for i in phone[-1:]:
            if i == '8':
                print(name,end=" ")
    print()
    return name

def num2():
    for p in d:
        val = p.values()
        val_list = list(val)
        name, phone, email = val_list
        
        if email == '':
            print(name)
    return name

def num3(user):
    find = False
    for p in d:
        val = p.values()
        val_list = list(val)
        name, phone, email = val_list
        if name.find(user.strip()) > -1 :
            print(phone, email)
            find = True
            break

    if find is False:
        print("이름이 없습니다.")

num1()
num2()
user = read()
num3(user)