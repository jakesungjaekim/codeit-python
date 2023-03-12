#덧셈
print(4 + 7) #11
#뺄셈
print(2 - 4) #-2
#곱셈
print(5 * 3) #15
#나머지
print(7 % 3) #1
#거듭제곱
print(2 ** 3) #8
#나눗셈
print(7 / 2) # 3.5
print(6 / 2) # 3.0
print(7.0 / 2) #3.5
print(6.0 / 2.0) #3.0
# floor division(버림 나눗셈): 나눈 결과 값에서 소수부분을 버린다!
print(7 // 2) # 3
print(8 // 3) # 2
# 특이점: 버림 나눗셈을 할 때 한가지가 소수형이면 결과값도 소수형으로 나온다.
print(8.0 // 3) #2.0 
print(8 // 3.0) #2.0
#round function
# round(반올림)
print(round(3.145926535))
# round(반올림)
print(round(3.145926535, 2))
# round(반올림)
print(round(3.145926535, 4)) 

print('======================================')

print('Codeit')
print('Jake')
print('I\'m excited to learn Python')
print("I'm excited to learn Python")
print("Hello " + "World")
print('7' + '6')

print('======================================')

print(int(3.8)) # 3
print(float(3)) 
print(int("2") + int("5")) 
print(float("2") + float("5")) 
print(str(2) + str(5)) 
age=7
print("제 나이는" + str(age) + "살 입니다")
# print(int("Hello World")) # 오류 -> 논리적이지 않음

print('======================================')

#오늘은 2019년 10월 29일입니다.
year = 2019;
month = 10;
day = 29;
#문자열 포맷팅
print('오늘은' + str(year) + '년' + str(month) + '월' + str(day) + '일입니다.')
print('오늘은 {}년 {}월 {}일입니다.'.format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
#문자열 포맷팅 응용: 출력 순서 바꾸기
print("저는 {},{},{}를 좋아합니다".format('jake','codeit','ENTJ'))
print("저는 {1},{0},{2}를 좋아합니다".format('jake','codeit','ENTJ'))
#포맷팅 응용: 소수점 절사
num_1 = 1 
num_2 = 3
print('{0} 나누기 {1}은 {2}입니다.'.format(num_1, num_2, num_1 / num_2))
print('{0} 나누기 {1}은 {2: .2f}입니다.'.format(num_1, num_2, num_1 / num_2))
print('{0} 나누기 {1}은 {2: .4f}입니다.'.format(num_1, num_2, num_1 / num_2))
print('{0} 나누기 {1}은 {2: .0f}입니다.'.format(num_1, num_2, num_1 / num_2))

print('======================================')
#불린 (Boolean): 따옴표 없이 작성
print(True)
print(False)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(2 > 1)
print(2 < 1)
print(3 <= 3)
print(2 != 2)

print('======================================')
print(type(3))
print(type(3.0))
print(type("3"))
print(type(True))
def Hello():
    print("Hello World")
print(type(Hello))
print(type(print))