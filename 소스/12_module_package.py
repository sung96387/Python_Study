# 12_module_package.py
# module폴더 : 패키지
# module\__iniy__.py : 패키지의 초기 설정 파일
# module\myModule.py : 직접 만든 모듈
# module\main.py : myModule을 import하는 용도의 테스트 프로그램 (일종의 모듈)
# module\__pycache__ 폴더 : 무시!!
'''
    [모듈과 패키지]

      모듈 (module)
        - 변수,함수,클래스 등을 모아 놓은 스크립트 파일
        - 간단한 기능을 담을 때 사용
        - 다른 파이썬 프로그램에서 불러와 사용할 수 있게
          만들어진 파이썬 파일(.py)

(모듈 관련 내용은 module폴더를 참고!)
  1) myModule.py : import 시킬 모듈
  2) main.py : myModule을 import해서 사용할 일종의 모듈

      패키지 (package)
        - 여러 모듈을 묶은 것 --> module 폴더가 즉 패키지
        - 하나의 파이썬 파일(모듈)에서 모든 기능 수행을
           정의하기가 어려울 때 (규모가 클 때 사용)
        - 관련 있는 모듈들을 묶어놓은 것

        - 폴더 안에 __init__.py 파일이 있어야 해당 폴더가 패키지가 된다.
          (파이썬 3.3. 버전부터는 __init__.py파일이 없어도 된다.)

        - __init__.py 의 기능
           > module에 있는 파일 참고

        - 패키지의 하위 패키지도 동일하게 . 을 붙여서 따라간다.
         import pack1.pack2.pack3.pack4.module

'''
#현재 시스템에 저장되어 있는 경로(생략해도 자동으로 찾아가는 경로)
# 절대경로/상대경로
'''
import sys # sys 모듈 혹은 패키지
print(sys.path) # 모듈 안에 있는 변
'''
# sys.path에 모듈이나 패키지가 존재해야한다.
# sys.path.append("C://test") 이런식으로 리스트에 요소를 추가해서 사용 가능

# 패키지의 모듈을 사용
# 현재 이 파일은 moudle폴더와 경로가 다르다!

'''
import module.myModule # 동일하게 as나 from으로 이름을 줄이거나 생략 가능!
print(module.myModule.my_string)
'''
# 1) from . import myModule 했을 때
'''
import module
print(module.myModule.my_string)
# 패키지만 import 하면,
# 패키지에서(__init__) import할 모듈 지정
'''

# 2) from.myModule import * 했을 때
'''
import module
print(module.my_string)
# 패키지에서 myModule의 모든 것을 import함
'''
# 3) __all__ 사용
'''
from module import *
print(my_string)
print(my_add(1,2))
# print(my_pow(2,3)) # 2^3 
# 오류 my_pow는 __all__에 포함되어 있지 않다.

'''





