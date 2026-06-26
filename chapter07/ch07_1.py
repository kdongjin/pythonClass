# 함수

# 함수선언
def open_func():
  print("드디어 함수 시작입니다.")

open_func()  

# 함수선언(매개변수)
def add_func(number1, number2):
  print("덧셈을 계산하는 함수입니다.")
  return number1 + number2

sum = add_func(10, 20)
print(f" add_func(10, 20) 결과값은 {sum}입니다.")

# 함수 기본값 설정
def profile(name, age=30, main_subject = "자바"):
  print("나의이름: {} , 나이는 {} ,메인언어는 {} ".format(name, age, main_subject))

profile("kdj",61,"C") 
profile("홍길동", 50) 
profile("저길동")

# 가변인자  *가변인자변수명
def new_profile(name, age, lang1, lang2, lang3):
  print(name, age, lang1, lang2, lang3)

def new_profile2(name, age, *language):
  print(name, age)
  print(language, type(language))  #('c', 'cpp', ~~) <class 'tuple'>
  for lang  in language:
    print(" {} ".format(lang), end=" ")
  print("")

new_profile2("kdj",62, "c", "cpp", 'java','spring')
new_profile2("kdj",62, "c")





