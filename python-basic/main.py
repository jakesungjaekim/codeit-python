burger_price = 4990
potato_price = 1490
beverage_price = 1250



print(burger_price)
print(burger_price*2)
print(burger_price + potato_price)
print(burger_price*3 + potato_price*2 + beverage_price*5)

# 파라미터
# name 을 Parmameter라고 지칭함
# 함수 안에는 argument 겠군! ㅎ
def hello(name): 
    print("Hello!")
    print(name)
    print("Welcome to CodeIt")
          
hello("Jake")

def print_sum(a, b, c=0):
    print(a+b)
    print(a*b)
    print(a+b+c)

print_sum(1, 3 )
print_sum(1, 3, 4)

