# 번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.

# 당첨 액수는 아래 규칙에 따라 결정됩니다.

# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)

import random

# 6개의 번호를 뽑는다.(배정 받는다.)
# 7개의 당첨번호를 뽑는다. 
# 번호를 비교하고
# 비교한 것이랑 기준이랑 비교해서 상금을 부여한다.


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = random.randint(1,45)
        if num not in numbers:
            numbers.append(num)
        
    return numbers

print(generate_numbers(6))

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print(draw_winning_numbers())

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    
    return count

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 100000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5 :
        return 10000000
    elif count == 4 :
        return 50000
    elif count == 3 :
        return 1000
    else:
        return "꽝"
    
    
        




# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
print(check([2, 4, 11, 14, 25, 40], []))
