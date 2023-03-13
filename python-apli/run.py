# 같은 폴더 안에 있는 파일만 불러올 수 있음. 이를 모듈이라고 지칭한다.
# calculator 라는 모듈을 calc라 지칭해서 사용하겠다.
import calculator as calc 

# 모듈 사용 법
print(calc.add(2, 5))
print(calc.multiple(3, 4))


# 칼큘레이터 모듈에서 저 함수만 가져와서 사용한다는 뜻
from calculator import add, multiple 
print(add(2,5))
print(multiple(3,4))

# 모든 칼큘레이터 함수를 가져오는 방법
# 하지만, 권장하지는 않는 방법이다.
# from calculator import *