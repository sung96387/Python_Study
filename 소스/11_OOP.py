'''  지금부터 하는 내용은 절대로 쉬운 내용은 아니다!
     다른 과목같은 경우는 이 내용만으로 몇 주를 다룬다.
     중간에 줄을 한번 멘탈 와르르 깨진다.
       (이런게 있고 이렇게 사용하는 거구나~!.)
     실제 실무에서도 완벽하게 객체지향 프로그래밍을 구현 ! --> X
     
    [Object Oriented Programming] 객체지향 프로그래밍
      - 객체지향이론
          실제 세계는 사물(객체)로 이루어져 있으며,
          발생하는 모든 사건들은 사물 간의 상호작용이다!!

      - 특징
        1. 코드의 재사용성이 높다. (함수의 장점과 비슷)
        2. 코드의 관리가 용이하다.
        3. 신뢰성이 높은 프로그래밍을 가능하게 한다.

      - '클래스' 와 '객체'
        1. 클래스는 일종의 설계도(또는 틀)이며,
           객체는 그 설계도를 통해 만들어진 실제 사물이다.
              아이폰7 설계도 -->아이폰 7(S/N : 1)
                                아이폰 7(S/N : 2)
              철인 로보트 설계도 --> 철인 28호, 철인 29호, 철인 30호....

        2. 클래스(class)
            - 정의 : 객체를 정의해 놓은 것
            - 용도 : 객체를 생성

        3. 객체 (object)
            - 정의 : 실제로 존재하는 것. (실제사물)
            - 용도 : 정의해놓은 클래스에 따라 다르다.
            - 유형의 객체 : 책상, 의자, 모니터, 컴퓨터 등
            - 무형의 객체 : 수학공식 같이 '개념'적인 것

        - 객체와 인스턴스
          > 인스턴스 (instance)
             - 기본적으로 객체와 같은 의미
             - 클래스를 통해 실제로 만들어진 객체를 인스턴스라고 부른다. (표현의 차이)
                 철인 설계도는 클래스다.
                 그 클래스로 만들 수 있는 철인은 객체이다.
                 철인28호는 인스턴스이다.

        - 객체의 구성 요소 - 속성과 기능 (클래스에서 정의한)
            1. 객체는 다수의 속성과 기능을 가지고 있다.
            2. 속성 : 변수
            3. 기능 : 함수 (클래스 안에 정의된 함수는 메서드라고 부른다.)

        * 클래스 = 변수 + 함수
        * 객체 = 클레스에 정의된 변수와 함수를 사용

        * 클래스를 만들때(설계할때) 특징을 잘 고려한다.
         > 변수와 함수의 연관성을 고려한다.

         ex) 철인 클래스
             속성(변수) : 이름(28호), 연료(10만cc), 무기(칼), 내구도(HP : 100)
             기능(함수) : 달리기, 때리기, 자폭하기
                                          >> 자폭 = 내구도가 0일때 자폭한다!
'''

'''
# 일단 클래스를 만들어서 사용해보기!!

class Car : # 여기서부터 자동차 설계도를 정의하기 시작!(설계 단계)

    # self를 반드시 넣어줘야한다.(이름은 중요하지 않다)
    #   > 이 함수가 호출됐을 때, 함수를 호출한 인스턴스 자기 자신을 의미한다.
    #   > 이 함수를 호출할때 self에 들어갈 값을 따로 넣어주는게 아니다.
    #   > bmw.powerOn() 을 했을때 self는 bmw가 된다.
    
    # 클래스 안에 함수를 정의(기능)
    def powerOn(self) : # 클래스 안의 함수(메서드)는 반드시 1개 이상의 매개변수 필요
        print("부릉부릉")
        self.power = True # 시동을 걸면 전원이 켜진다 (True)
    # 얘는 밖에서 bmw.power = True를 한 것과 같다.
        self.drive() # 메서드 안에서 다른 메서드를 호출!
        # bmw.drive() --> self = bmw 

    def drive(self) :
        print("주행을 시작합니다.")

# 객체 만들기!(인스턴스 생성)
# 인스턴스명 = 클래스명()
bmw = Car()
# Car 클래스를 통해서 실체가 만들어지고, 그 실체를 bmw 변수에 대입

# print(bmw.power) # 오류! -> 이 때는 power 속성이 없다!

# 인스턴스를 가리키는 변수를 통해, 기능 사용! (외부에서 클래스의 함수 접근/사용)
bmw.powerOn() # 이 함수를 호출하고나면, bmw는 power라는 속성이 생겼다.
print(bmw.power)

tico = Car() # 위에있는 bmw와는 다른 또다른 자동차이다! (인스턴스/객체가 새로 만들어짐)
tico.powerOn() # 이 때 powerOn에서의 self는 tico

# 이와 같은 방식으로 Car() 를 이용하면 동일한 속성/기능이 정의된 자동차들을 만들 수 있다.
print("="*20)

# 1. 클래스를 왜 사용할까??
print("***클래스 사용 안할때***")
# 자동차를 3대 만들기 : 모델명, 시동on/off 여부(power), 최고속도
car1_model = "BMW"
car1_power = False # 꺼져있다.
car1_max_speed = 200

car2_model = "SONATA"
car2_power = True # 켜져있다.
car2_max_speed = 180

car3_model = "TICO"
car3_power = True # 켜져있다.
car3_max_speed = 150

# 자동차가 주행하는 함수 만들기(시속 몇km로 주행하겠다!)
def drive_car(power,speed,max_speed,model) :
    print("{} 자동차 주행준비".format(model))

    if power == False :
        print("시동을 켜주세요!!")
        return # return만 그냥 쓰면 반환되는 값이 없고 함수 끝 (반복문의 break처럼)

    if speed > max_speed :
        print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(model,max_speed))
        # 전달된 speed의 값을 max_speed 값으로 변경
        speed = max_speed
    print("{}km로 주행합니다.".format(speed))


drive_car(car1_power,180,car1_max_speed,car1_model) # BMW
drive_car(car2_power,200,car2_max_speed,car2_model) # SONATA
drive_car(car3_power,300,car3_max_speed,car3_model) # TICO

# 각 자동차를 주행시키기 위해 함수 호출시 각 자동차의 정보를 매개변수로 전달
# 이때 car1_xxx, car2_xxx 이렇게 구분을 하긴 했지만, 서로 관련있는 변수들 아니다!

print("="*20)

# 2. 클래스의 사용 (1)
print("***클래스 사용 할때(1)***")

class Car :
    # self 가 필요.
    # 자동차의 공통속성 power, max_speed,model --> self에 들어있다!!
    def drive_car(self,speed) :
        print("{} 자동차 주행준비".format(self.model))

        if self.power == False :
            print("시동을 켜주세요!!")
            return # return만 그냥 쓰면 반환되는 값이 없고 함수 끝 (반복문의 break처럼)

        if speed > self.max_speed :
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model,self.max_speed))
            # 전달된 speed의 값을 max_speed 값으로 변경
            speed = self.max_speed
        print("{}km로 주행합니다.".format(speed))

car1 = Car() # 자동차 인스턴스(객체)가 하나 만들어 지고 그걸 car1이 가리킨다. 
car1.model = "BMW"
car1.power = False # 꺼져있다.
car1.max_speed = 200

car2 = Car() # 위에 있는 자동차랑 상관 없이, 새로운 자동차가 만들어진것
car2.model = "SONATA"
car2.power = True # 켜져있다.
car2.max_speed = 180

car3 = Car()
car3.model = "TICO"
car3.power = True # 켜져있다.
car3.max_speed = 150

# 이렇게 호출하면 drive_car(self,speed)에는
# self에는 각각의 car1,car2,car3 이 들어가고, speed는 아래 값들이 들어간다.
car1.drive_car(180)
car2.drive_car(200)
car3.drive_car(300)
    
# 이 단계에서는 함수 매개변수로 전달해야할 값들을 하나의 객체에 담아서 전달!
# 아까는 서로 관계가 없던 변수들이 관계가 형성되었다.

print("="*20)

# 3. 클래스의 사용 (3) -생성자
# 생성자 : 인스턴스 생성 시 자동으로 호출되는 함수(매서드)
print("***클래스 사용 할때(2)***")
# __init__ 이 이름은 규칙! 생성자를 의미한다.
# 생성자는 인스턴스 생성과 동시에 초기화 하고 싶을 때 사용 
class MyClass :
    def __init__(self,name2) :
        print("생성자가 호출됩니다.",name2)
        self.name = name2 # m1.name = "홍길동" // m2.name = "임꺽정"
        # name은 단순히 매개변수로 전달된 값일 뿐이고,
        # self.name 을 한 것이 객체의 속성을 만든 것
        
m1 = MyClass("홍길동") # 인스턴스를 생성하는 행위 : MyClass()
m2 = MyClass("임꺽정")
# 생성자가 호출되면서, m1과m2는 name이라는 속성이 생겼다!!!

print(m1.name)
print(m2.name)

print("="*20)

# 연습문제!!!!!
# 4. 클래스의 사용(4) - 위에 있는 클래스의 사용(1)을 생성자를 이용하여 코드를 줄인다.
class Car :
    def __init__(self,model,power,max_speed):
        print("생성자가 호출됩니다!")
        self.model = model
        self.power = power
        self.max_speed = max_speed
        # self. 하는 것은 내 객체(인스턴스)에 변수(멤버)를 추가하는 것!
        # 뒤에 대입이 되는 변수들은 생성 시 매개변수로 전달된 값들
    def drive_car(self,speed) :
        print("{} 자동차 주행준비".format(self.model))

        if self.power == False :
            print("시동을 켜주세요!!")
            return 
        if speed > self.max_speed :
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model,self.max_speed))
            speed = self.max_speed
        print("{}km로 주행합니다.".format(speed))

car1 = Car("BMW",False,200) # 자동차 인스턴스(객체)가 하나 만들어지고 그걸 car1이 가리킨다
car2 = Car("SONATA",True,180) # 위에 있는 자동차랑 상관없이, 새로운 자동차가 만들어진다
# 원래는 Car() 이렇게 해서 인스턴스(객체)를 만들어 놓고,
# car2.~~~~ 해서 멤버를 추가하는 형태였지만..
# 생성자를 통해서 생성과 동시에 멤버들을 추가를 한 형태가 되었다!
car3 = Car("TICO",True,150)

car1.drive_car(180)
car2.drive_car(200)
car3.drive_car(300)

print("="*20)

# 메서드 = 클래스 내부에 정의된 함수

# 5. 변수와 메서드(함수)의 종류
# 클래스 변수, 클래스 메서드    : 공통으로 사용하는 변수/메서드
# 인스턴스 변수, 인스턴스 메서드 : 해당 인스턴스가 사용, 인스턴스만 사용
'''
'''
    - 클래스 변수
         1. 클래스 내부에서 생성(engine="1000cc")
         2. 클래스 메서드에서 생성 (cls.value =10)
         3. 클래스 외부에서 클래스명을 통해 생성 (Car.wheel = 4)
    - 인스턴스 변수
         1. 생성자 생성 (self.power)
                --> 모든 인스턴스는 공통으로 이 변수가 생성
         2. 인스턴스 메서드에서 생성 (self.Navi)
                --> 호출한 인스턴스만 생성이 됨 (car1)
         3. 클래스 외부에서 인스턴스를 통해 생성 ( car1.sun_roof = "썬루프")
                --> 해당 인스턴스에만 생성
                
     * 클래스 변수는 한 번 만들어 지면 클래스나 인스턴스가 접근 가능하고, 값이 공유된다.
       인스턴스 변수는 인스턴스 별로 독립적이다.

     * 클래스메서드 : 클래스명 또는 인스턴스로 사용 가능
                --> 클래스명으로 사용을 하자!

     * 인스턴스메서드 : 인스턴스로만 사용 가능
                --> self를 매개변수로 사용. 이 때의 self는 나 자신 인스턴스(호출한 인스턴스)
'''
'''

class Car :
    engine = "1000cc"  # 클래스 변수

    def __init__(self) :
        self.power = True # 인스턴스 변수

    def instMethod(self) :
        print("인스턴스 메서드")
    def instMethod2(self) :
        self.Navi = "네비게이션"

    @classmethod # 메서드 정의 위에 이걸 붙여야 클래스 메서드가 된다.(장식자/데코레이터)
    def classMethod(cls) : # cls = 클래스 자기 자신을 의미!
        print("클래스 메서드")
        cls.value = 10 # 클래스 변수

# 클래스 변수는 인스턴스 생성과 상관없이, 클래스가 정의되면서 만들어지는 변수
print(Car.engine)

car1 = Car() # 인스턴스 생성! -> 이때 car1에게는 power 멤버변수가 생성된 상태

# 클래스변수 사용
print(Car.engine) # 클래스명.변수명   <--- 사용!!
print(car1.engine) # 참조변수로도 사용이 가능하다
# 하지만 클래스 변수는 클래스의 하나인 변수이므로 클래스명. 해서 사용!!!!

print(car1.power) # 인스턴스로 인스턴스 변수 사용
# print(Car.power) # 오류 --> 클래스명으로는 인스턴스변수를 사용할 수 없다!!! (절대!!)
# self. ~~ 인스턴스명.~~~ 만든 것들은 클래스명으로 사용 못한다.

Car.wheel = 4 # 자동차 바퀴는 4개!! -> 클래스변수 추가
print( car1.wheel)

car2 = Car() # 인스턴스 생성! 이 친구는 power만 가지고 있다.

car1.sun_roof = "썬루프" # car1 인스턴스에 멤버변수 추가

# print(car2.sun_roof) # sun_roof는 car1에게만 만들어진 인스턴스 변수이다! (car2는 없다)
print(car1.sun_roof) # car1은 사용됨 (내꺼니까)

car1.wheel = 8 # car1 자동차는 트럭! 나는 바퀴가 8개 야~
# 클래스 변수  wheel이 아닌 인스턴스 변수 wheel을 car1에 추가됨
# print(car1.wheel) #을 했으면, 이미 클래스변수 wheel이 있기 때문에 4를 사용.
# car1.wheel = 8 <-- 값의 대입!! 인스턴스변수로 취급 (클래스 변수의 값을 바꾸는게 아님!!)

print(car2.wheel) # 위에서 만들어진 클래스 변수!


car1.instMethod() # 인스턴스 메서드 사용!
# Car.instMethod() # 오류 --> 클래스명으로는 인스턴스 메서드 사용 불가
# print( Car.value ) # 이 때는 아직 classMethod가 호출되기 전이라 클래스 변수가 없다.
Car.classMethod() # 클래스 메서드 사용! (클래스명.메서드명)
print( Car.value ) # 메서드에서 10으로 값을 세팅!

Car.value = 20 # 내가 임의로 20으로 변경!
print( Car.value )

car1.classMethod() # 인스턴스로 클래스 메서드 호출 가능!
print( car1.value ) # 인스턴스로 클래스변수 사용! (메서드에서 다시 10 으로 바꿨다)

car1.instMethod2()
print(car1.Navi)
print(car2.Navi) # car2는 Navi가 없다! ㅠㅠ
'''
# 외부 : 클래스의 외부


# 6. 외부 접근 제어 : public / private
#        클래스 외부에서 클래스 내부를 접근하는 것에 대한 제어 (할 수 있다/없다)
# public : 외부 접근 가능  : 그냥 사용 하면 public
# private : 외부 접근 불가 : 이름앞에 __(언더바2개) 붙이면 됨.

class Person : # 사람이라는 클래스
    name = "이몽룡"  # public 클래스 변수
    __addr = "서울시 강남구" # private 클래스 변수

    def __init__(self) :
        self.__age = 1

    def print_info1(self) :
        print("{}님은 {}살이며, {}에 거주합니다".format(self.name ,self.__age,self.__addr))

    def __print_info2(self) : # private 인스턴스 메서드
        print("{}님은 {}살이며, {}에 거주합니다".format(self.name,self.__age ,self.__addr))

    def print_infoAll(self) :
        self.print_info1()
        self.__print_info2()

    def set_age(self,age) :
        if age < 1 :
            age = 1
        elif age > 200 :
            age = 200
        # 위 두 조건을 만족하지 않으면, 1~200 사이라는 것이고, 이 값은 유효하다고 판단
        self.__age = age

    def get_age(self) :
        return self.__age # 외부에서 접근 불가능한 __age의 값을 반


person = Person()
# person.__age = -1 # 사람의 나이는 음수가 될 수 없다!! (논리적으로 보았을때)
# 이 행위는 클래스에 선언된 __age에 값을 넣는 것이 아니라 , 또 다른 새로운 __age가 생긴것

# set_age 라는 메서드를 통해 클래스 내부의 __age 값을 세팅
person.set_age(-1) # -1을 넣는 다는 것은 뻘짓 !! 사람나이는 음수 x
# 함수 내부에서 -1을 강제로 1로 변경 

print(person.name) # 접근 가능
# print(person.__addr) # 외부에서 접근 불가
    
person.print_info1() # 접근 가능
# person.__print_info2() # 외부에서 접근 불가

person.print_infoAll() # 통합된 메서드로 private을 외부에서 우회 접근

'''
     클래스를 만든 사람 // 클래스를 사용하는 사람

        클래스를 사용하는 사람이 논리적으로 말이 안 되는 행위를 할 수 있다!
        (나이라는 변수에 -1을 대입)

        이 행위를 클래스를 만든 사람이 미리 차단/예외처리를 한것
        private으로 외부에서 변수에 마음대로 접근할 수 없도록 차단하고,
        변수의 값을 변경하고 싶으면 메서드를 통해 변경하도록 했다.
         private : 외부 접근 불가 --> 클래스 정의 내부에서는 얼마든지 사용 가능

        __age라는  private 변수의 값을 세팅하는 메서드 : setter 라고 부른다
        __age의 값을 반환하는 메서드 : getter 라고 부른다!!

        getter와 setter 메서드의 이름은, get변수명, set변수명 이런식으로 명시
'''
# print(person.__age)
print(person.get_age()) # getter의 사용
print()

#7 상속 (inheritance)
'''
    - 무언가를 물려받는다.
    - 클래스의 상속
        기존의 정의해놓은 클래스의 기능을
        '그대로' 물려받는 새로운 클래스를 정의한다.

    - 기반클래스 : 부모클래스, 슈퍼클래스
    - 파생클래스 : 자식클래스, 서브클래스

    - 자식클래스에서는 부모클래스의 변수,메서드를 사용가능한다.

    - 메서드 오버라이딩 (method overriding) [재정의]
       > 자식클래스에서 부모클래스에 이미 정의된 메서드를 다시 정의하는 것
       > 자식클래스의 인스턴스는 오버라이딩된 메서드가 호출된다. (부모의 메서드 무시)
'''
class Person : # 사람 클래스 정의
    def __init__(self, name, age) : # Person("홍길동",20)
        print("Person, 생성자 호출({})".format(name))
        self.name = name
        self.age = age

    def print_info(self) :
        print( "Person, print_info 호출" )
        print( "이름 : ",self.name)
        print( "나이 : ",self.age)

    def sleep(self) :
        print("Person, sleep 호출")
        print("{}님은 8시간 잡니다.".format(self.name))
# 상속 받은 자식 클래스 2
class Student(Person) : # 상속 받을 클래스 명을 () 안에 넣어준다
    def study(self) :
        print("Student, study 호출")
        print("{}님은 6시간 공부합니다.".format(self.name))

    def sleep(self) : # Person, 상속 받은 클래스의 메서드를 다시 정의 -> 오버라이딩
        print("Student, sleep 호출")
        print("{}님은 6시간 잡니다.".format(self.name))
# 상속 받은 자식 클래스 2
class Teacher(Person) :
    #def __init__(self) : # (1) 아무것도 사용하지 않는 생성자
     #   print("Teacher, 생성자 호출")
     # 이렇게 생성자를 만들면 name,age가 없다..! (Person 의 생성자에서 name,age를 생성)
    def __init__(self,name,age):
        super().__init__(name,age) # super() : 부모클래스를 의미
                                                 #  --> Person의 생성자 직접호출
                                                 #      중복되는 인스턴스변수 생성 코드 제거
        # 더 명확하게 호출하는 것. 위와 똑같다. 생략 가능
        # super(Teacher,self).__init__(name,age)

    def sleep(self) :
        print("Teacher, sleep 호출")
        super().sleep() # 부모클래스의 원래 sleep 메서드를 직접 호출
        print("선생님은 그렇게 많이 자면 안됩니다...")

    def work(self) :
        print("Teacher, work 호출")
        print(self.name + " 선생님은 6시간 일 합니다 .")
        
       # self.name = name
       # self.age = age
        # 인스턴스 변수 생성 --> 코드의 중복 발생!
        # Person생성자에서 이미 name,age를 만들고 있다.
        
#######################################################

# Person 클래스의 인스턴스 생성
p_hong = Person("홍길동",20)
p_hong.print_info()
p_hong.sleep()
print()
# Student 클래스의 인스턴스 생성
# 자식클래스에는 생성자가 없지만, 상속받은 클래스의 생성자가 호출된다.
s_sung = Student("성춘향",19)
s_sung.print_info() # 상속받은 메서드 사용 가능
s_sung.study() # 나만 가지고 있는 메서드
s_sung.sleep() # 원래 Person의 sleep이 호출 됐지만, 오버라이딩 후 Student의 sleep 호

# p_hong.study() # person에는 study가 없다. 사용불가!
t_lee = Teacher("이몽룡",30)
t_lee.print_info()
t_lee.sleep() # 오버라이딩 되어서 Person의 sleep은 사용 할 수 없다.
t_lee.work()
# 8. 추상 클래스 (상속 관계 사용시 사용할 수 있는 개념)
'''
    추상적이다!
        - 동물(Animal)이라는 클래스를 정의하면서,
        동물은 '울음운다'라는 기능이 있다고 추상적인 개념만 정의 해놓고
        각 동물들이 실제로 어떻게 우는지는 Animal을 상속받은 자식클래스에서
        직접 정의하도록 하는 것

        - 이때 '울음운다' 라는 기능(메서드)을 '추상메서드'라고 한다
         추상메서드는 상속받은 클래스에서 '반드시' 오버라이딩(정의)해야 한다.
        - 추상메서드가 있는 클래스를 '추상클래스'라고 한다.
        
        - 자식 클래스에서 '반드시' 추상메서드를 정의하도록 강제성 부여

[사용 방법]
abc (모듈) 필요 (abstract base class)   -> abstract class = 추상 클래스
from abc import *

class 추상클래스명(metaclass = ABCMeta) :
    @abstractmethod
    def abstract_method(self) : 
        ~~~
'''
print()
from abc import * # abc 모듈은 파이썬 설치 시 자체 내장

class Animal(metaclass = ABCMeta) : # 나는 추상클래스다!!
    @abstractmethod
    def Cry(self) :
        print("동물은 소리내어 운다....")
class Dog(Animal) :
    def info(self) :
        print("나는 개다")

    def Cry(self) : # 반드시 정의해야하는 추상메서드 정의
        print("멍멍")
class Cat(Animal) :
    def Cry(self) : # 반드시 정의해야하는 추상메서드 정의
        print("야옹야옹")
dog = Dog()
dog.info()
cat = Cat()
cat.Cry()
# 클래스 연습하기
'''
    1. 학생 클래스 (Student)
        속성 : 이름, 나이,전화번호,과목
        기능 :
              - 학생정보 출력 (print_info)  --> 아래 내용 출력하는 기능
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-1234

              - 공부하기 (study) -> 아래내용 출력하는 기능
                  홍길동 님이 파이썬 공부를 시작합니다


        3명 이상의 학생을 만들어서, 정보출력 및 공부하기 실행
'''
class Student :
    def __init__(self,name,age,number,subject):
        self.name = name
        self.age = age
        self.number = number
        self.subject = subject
    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("나이 : {} ".format(self.age))
        print("전화번호 : {} ".format(self.number))
    def study(self) :
        print("{}님이 {} 공부를 시작합니다.".format(self.name,self.subject))

s1 = Student("홍길동",20,"010-1234-4567","파이썬")
s2 = Student("장길동",21,"010-1234-4567","C++") 
s3 = Student("박길동",22,"010-1234-4567","자바")

s1.print_info()
s2.print_info()
s3.print_info()
s1.study()
s2.study()
s3.study()
'''
    2. 계산기 클래스(Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 기억하는 변수들
                 add_count, min_count, mul_count, div_count
        기능 : 사칙연산(4개), 정보출력(print_info)

        굳이 계산 값과 어떤 연산을 할 지 입력받아서 하지 않아도 됨!!
        add(1,2) 그냥 이런식으로 호출하고, print_info의 결과가 제대로 나오는지 확인

        [출력결과]
        1 + 2 = 3
        4 - 2 = 2
        (print_info를 수행했을때!!)
        덧셈 : 1
        뺄셈 : 1
        곱셈 : 0
        나눗셈 : 0

    3. MyData 클래스
           (1) 외부에서 접근 불가능한 변수를 하나 만들기
           (2) getter,setter 만들기
           (3) 이 변수가 가질 수 있는 값의 범위는 1 ~10
               1 미만 : 1 로 세팅
               10 초과 : 10 세팅
           (4) 인스턴스를 3개 만들고, 각각 1미만,10초과, 1~10의 값을 넣고
           (5) getter를 이용하여 값 출력

    4. 책을 의미하는 Book클래스
       전자책을 의미하는 eBook 클래스

       책 : 제목, 정가
       전자책 : 제목, 정가, 보안키

       (상속 관계 성립 시켜야함)

     print_info()는 오버라이딩 해야한다. (단, 중복된 코드는 최소화)
       [메서드 호출 시 출력결과]
       python_book.print_info()
       제목 : 파이썬 최고
       정가 : 20000원

       pyhton_ebook.print_info()
       제목 : 파이썬 최고 - ebook
       정가 : 10000원
       보안키 : ab-123

    5. 사각형을 의미하는 Rectangle 클래스
       정사각형을 의미하는 Square 클래스
       (상속 관계 성립 필요!)

       print_area() 는 오버라이딩 하지 않는다.


    rect = Rectangle(3,4)
    rect.print_area()
    면적 : 12

    sqr = Square(7) # 한 변의 길이
    sqr.print_area()
    면적 : 49
    

'''










