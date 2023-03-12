#지정 연산자
name = '김성재'
x = 7 
x = x + 1 # 지정 연산자 (assignment operator)
print(x) # 8
x = 7
x = x - 3
print(x) # 4
print('=================================')

#함수의 실행 순서
def hello():
    print('Hello')
    print("Welcome to Codeit")

print("함수 호출 전")
hello()
print("함수 호출 후")
print('=================================')
def square(x):
    return x * x

print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")
print('=================================')
def square(x):
    print("함수 시작")
    return x * x
    print("함수 종료") ## 데드코드

print(square(3))
print("Hello Jake?")
print('=================================')
# return과 print의 차이

def print_square(x):
    print(x * x)
    # return None 생략되어있음.

def return_square(x):
    return (x * x)

print(print_square(3)) # 9 , None
print(return_square(3)) # 9
print('=================================')

#scope
def my_function():
    x = 3
    print(x)

my_function()
print(x)

#상수
PI = 3.14 
def calculate_area(r):
    return PI * r * r

radius = 4 
print("반지름이 {}면, 넓이는{}".format(radius, calculate_area(radius)))
