def recur_function() :
    a = input("write your line : ")
    if a.isdigit():
        a = int(a)
        if a % 2 == 0:
            print(int(a / 2))
            recur_function()
        else:
            print((a * 3) + 1)
            recur_function()
    elif a.lower() == "cancel":
        print("bay")
    else:
        print('your line is not number')
        recur_function()

recur_function()