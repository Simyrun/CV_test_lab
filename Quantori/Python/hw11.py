def alfabet_1(start, stop, step=0):
    answer = []
    a = 0
    start = ord(start)
    stop = ord(stop)
    if start == stop:
        print(answer)
    if step == 0:
        answer.append(chr(start))
        a = int(stop - start) - 1
        while a > 0:
            a -= 1
            start += 1
            if chr(start) not in answer:
                answer.append(chr(start))
    if step > 0:
        answer.append(chr(start))
        a = abs(int((stop - start) - 1) - 10)
        while a >= 0:
            a = a - abs(step)
            a -= 1
            start += step
            answer.append(chr(start))
    if start > stop:
        answer.append(chr(start))
        a = int(start - stop)
        while a >= 0 or (a - abs(step)) <= 0:
            a = a - abs(step)
            a -= 1
            start = start - abs(step)
            if start > stop:
                answer.append(chr(start))
            else:
                break
    return answer


print(alfabet_1('d', 'v'))