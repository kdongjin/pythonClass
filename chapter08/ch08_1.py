# 표준 입출려기능

# input 입력받은값은 무조건 문자열이다.
# num = input("당신이 좋아하는 숫자입력 >>")
# print(num, type(num))   #7 <class 'str'>

# flag = input("당신을 여행을 좋아하시나요(True/False) >>")
# print(flag, type(flag))   #True <class 'str'>

# gender = input("당신을 성별입력해주세요(F/M) >>")
# print(gender, type(gender))   #F <class 'str'>

# 문자열 => 숫자형(int, float)  숫자형, 부울형 => 문자열(str)

# 당신의 나이을 받아서 출력하는 프로그램작성
# age = float(input("당신의 나이는>>"))
# print(age, type(age))
# print("당신의 나이는 "+ str(age) + "입니다")  #TypeError: can only concatenate str (not "float") to str
# print("당신의 나이는 {} 입니다".format(age))  
# print(f"당신의 나이는 {age} 입니다")  


# 출력관련된 기능

# print("파이썬" + "자바",end="")  #파이썬자바
# print("파이썬" , "자바")  #파이썬 자바
# print("파이썬" , "자바", "자바스크립트", "스프링부트",sep=" , ")  #파이썬 , 자바 , 자바스크립트 , 스프링부트
# print("파이썬" , "자바",sep="/",end=" ?")  #파이썬/자바 ?파이썬 자바
# print("파이썬" , "자바")

# 표준화면출력(기본print), 표준에러출력
# import sys
# print("파이썬" , "자바", sep=",", file=sys.stdout)
# print("파이썬" , "자바", sep=",", file=sys.stderr)

# 출력화면서식지정1 (자바: %10s  %-10s)  ljust(size): 왼쪽정렬, rjust(size): 오른쪽정렬
# scores = {"수학": 100, "영어":90, "국어": 70}
# print(scores, type(scores))  #<class 'dict'>

# for key  in scores.keys(): 
#   print("key = {}".format(key))

# for value  in scores.values(): 
#   print("value = {}".format(value))

# for key, value in scores.items():
#   # print("key = {}, value={}".format(key, value))
#   print(key.ljust(10), str(value).rjust(10), sep="/" ) 

# 출력화면서식지정2    zfill(사이즈)  : 전체사이즈를 설게하고 나머지공간을 0으로 채운다.
# for i in range(1,21):  # 1부터 20까지 진행
#   print("num : "+ str(i).zfill(3))  #num : 001 num : 002

# 출력화면서식지정3   format() 형식

print("{}".format(100))
print("{0}".format(100))
print("{}  {}".format(100, 200))    #100  200
print("{0}  {1}".format(100, 200))  #100  200
print("{1}  {0}".format(100, 200))  #200  100

print("{0: >10}".format(100))       #       100
print("{0:_>10}".format(100))       #_______100
print("{0:_>+10}".format(100))      #______+100
print("{0:_>+10}".format(-100))     #______-100


print("{0:,}".format(100000000000))     #100,000,000,000
print("{0:+,}".format(100000000000))    #+100,000,000,000
print("{0:+,}".format(-100000000000))   #-100,000,000,000

print("{0:>+30,}".format(-100000000000))    #              -100,000,000,000
print("{0:_>+30,}".format(-100000000000))   #______________-100,000,000,000

print("{0:f}".format(95.7867))     #95.786700
print("{0:.2f}".format(95.7867))   #95.79
print("{0:10.2f}".format(95.7867)) #     95.79



