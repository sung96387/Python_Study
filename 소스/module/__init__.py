# 이 파일은 기본적으로 없어도 된다.
# (필요 시 사용)

# 패키지를 사용하면 이 파일이 먼저 수행된다.
print("__init__.py 입니다." )

# 이 파일이 수행될 때
# 점(.) = 현재 폴더
# 1) 현재 폴더에서 myModule을 import하겠다!
# from . import myModule

# 2) myModule의 모든 것을 import하겠다!
# from . myModule import *

# 3) __all__사용
# import에서 * 이 __all__과 같다.
# 리스트 형태로 추가를 한다.
# 추가된 것만 import가 된다
# 공개하고 싶은 것만 공개하는 용도
__all__ = ["my_string","my_add"]
from.myModule import *
