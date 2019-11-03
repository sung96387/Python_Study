# myModule.py (소스 폴더 안의 module폴더)
# 변수 생성
my_string = "myModule의 문자열입니다."
# 함수 정의
def my_pow(num1, num2) : # num1의 num2 제곱 반환 (2,4) -> 2^4
    return num1 ** num2
def my_add(num1, num2) :
    return num1 + num2
def my_mul(num1, num2) :
    return num1 * num2
# 클래스 정의
class Dog :
    def __init__(self, name) :
        self.name = name
# Dog 의 인스턴스(객체)가 생성될 때(생성자)
# 전달된 name을 내 객체의 name을 만들면서 대입
    def cry(self) :
        print( "{} : 멍멍!".format( self.name ) )

# 위에까지는 변수나 함수나 클래스를 생성,정의만 한 것
# 사용하진 않음. (눈에 보이는 결과가 없었다.)
print("myModule.py 를 import 하였다!")

# 모듈을 import 한다는 것은... 해당 파일을 수행시킨 것!!
#  1) main.py가 myModule을 import 했다
#  2) main.py가 실행!(프로세스 실행)
#  3) 실행된 프로세스에서 myModule.py를 코드를 수행했다!
#  4) 실행된 프로세스는 import한 모듈의 모든 정보를 기억

print( "__name__ :", __name__ )
# myModule.py를 직접 실행 : __main__
# import가 돼서 실행된 경우 : myModule

if __name__ == "__main__" :
    print("이 파일을 직접 수행했을때 하고 싶은 코드 작성!")




