# main.py (소스 폴더 안의 module폴더)

# 아까 만들어놓은 myModule.py 를 사용해보기

# .py로 된 파이썬 파일은 모두 다 모듈이라고 보면 된다.
# import 를 이용해서 해당 파일을 불러올 수 있다. = 사용 가능

# 모듈 사용하기 (1) - 모듈명 그대로 사용
'''
import myModule
print( myModule.my_string )
result = myModule.my_pow(2, 2)
print("2^2 =", result)
'''

# 모듈 사용하기 (2) - 별칭 주기 (as)
'''
import myModule as my
print( my.my_string )
result = my.my_pow(2, 3)
print("2^3 =", result)
'''

# 모듈 사용하기 (3) - 모듈에서 일부만 가져오기 (모듈명 필요X)
#   다른 변수,함수,클래스는 사용X
'''
from myModule import my_string, my_pow
# myModule 에서 my_string과 my_pow를 추가시키겠다!!
#          from                       import
print( my_string )
result = my_pow(2, 4)
print("2^4 =", result)
'''

# 모듈 사용하기 (4) - 모듈에서 전체 가져오기 (모듈명 필요X)
from myModule import *
print( my_string )
result = my_pow(2, 5)
print("2^5 =", result)

# 클래스 사용
Baduk = Dog("바둑이")
Baduk.cry()

# 프로그램 규모가 커지면, 외부 모듈을 가져다 쓸 일이 많다.
# 변수,함수,클래스 등의 이름이 중복될 가능성이 높아진다.
#   import 모듈명 as 나만의별칭
#   import myModule as koreais_m1


