# 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수를 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.
# 화씨 온도 리스트: [40, 15, 32, 64, -4, 11]
# 섭씨 온도 리스트: [4.4, -9.4, 0.0, 17.8, -20.0, -11.7]



def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))

i = 0

while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]),1)
    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))
