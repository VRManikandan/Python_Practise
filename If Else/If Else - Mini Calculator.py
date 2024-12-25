a=int(input())
b=int(input())
formula=input("add/sub/multi/div:")


if (formula=="add"):
    print(a+b)
elif  (formula=="sub"):
    print(a-b)
elif  (formula=="multi"):
    print(a*b)
elif (formula=="div"):
    print(a/b)
else:
    print("invalid input")
