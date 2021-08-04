def find_missing(number):
    start = number[0]
    end = number[-1]
    result = sorted(set(range(start, end + 1)).difference(number))
    for i in result:
        if i == None:
            return "none"
        else:
            result = min(sorted(set(range(start, end + 1)).difference(number)))
            return result

test_list = input("Write you number line : ").split(' ')
for i in range(0, len(test_list)):  #цикл перевода строчного списка в числовой
    test_list[i] = int(test_list[i])



print(find_missing(sorted(test_list)))
