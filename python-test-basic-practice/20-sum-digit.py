# 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.
# 예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3(1 + 2)을 리턴합니다.
# 마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 거죠.
# 여러분이 해야 할 일은 두 가지입니다.
# sum_digit 함수를 작성한다.
# sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.


def sum_digit(num):
    
    total = 0
    str_num = str(num)


    for i in range(len(str_num)):
        digit = str_num[i]
        total += int(digit)
    return total

digit_total = 0 

for i in range(1,1001):
    digit_total += sum_digit(i)


print(digit_total)

