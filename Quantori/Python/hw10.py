number= int(input("write your number: "))
n=0
while True:
    if number == 1:
        print("In total, we get", n, "steps.")
        break
    else:
        if number % 2 == 0:
            number = int(number / 2)
            n+=1
            print(number)
        else:
            number=((number * 3) + 1)
            n+=1
            print(number)

# example 1:
# write your number: 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# In total, we get 7 steps.

#example 2:
# write your number: 39
# 118
# 59
# 178
# 89
# 268
# 134
# 67
# 202
# 101
# 304
# 152
# 76
# 38
# 19
# 58
# 29
# 88
# 44
# 22
# 11
# 34
# 17
# 52
# 26
# 13
# 40
# 20
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# In total, we get 34 steps.