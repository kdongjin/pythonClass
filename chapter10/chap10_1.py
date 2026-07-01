# 예외처리

# 두수를 입력받아서 나눗셈해서 결과값을 출력하는 프로그램 작성

# while True:
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>")) 
#     print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#     continue
#   except Exception as e:
#     print(e)
#     continue
#   finally:
#     print("finally")

#   break

# print("프로그램 종료")

# 오류를 사용자가 조건에 따라서 발생시킴

# while True:
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>")) 
#     # 조건을 설정 두수는 0 보다 크고, 10 보다 작거나 같아야만 계산실행, 다르면 예외발생
#     if (0 < num1 <= 10) and (0 < num2 <= 10) :
#       print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
#     else:
#       raise ValueError
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#     continue
#   except Exception as e:
#     print(e)
#     continue
#   finally:
#     print("finally")
#   break
# print("프로그램 종료")


#던더 메서드 만들고 실행하기 
# class SpecialClass():
#   def __init__(self):
#     print("생성자 발생하였습니다.")
  
#   # 자바 toString() 같다고 생각하면 됨. 
#   def __str__(self):
#     return "내가 만들고 싶은 문자열을 만들어서 전송합니다."
  
# sc = SpecialClass()
# print(sc)


# 사용자 정의한 예외처리를 설계한다. (정의한 메세지를 던지기 때문에 메세지 정의해야된다.)
class MyException(Exception):
  def __init__(self, message):
    self.message = message
  
  def __str__(self):
    return "{}메세지가 발생하였습니다".format(self.message)
  

# 사용자가 정의한(MyException) 예외처리로 진행
while True:
  try:
    num1 = int(input("number1 >>")) 
    num2 = int(input("number2 >>")) 
    # 조건을 설정 두수는 0 보다 크고, 10 보다 작거나 같아야만 계산실행, 다르면 예외발생
    if (0 < num1 <= 10) and (0 < num2 <= 10) :
      print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
    else:
      raise MyException("입력값 {0}, {1} 값이 범위안에 미 포함하는 ".format(num1, num2))
    
  except ValueError:
    print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
    continue
  except MyException as e:
    print("오류가 발생했습니다. 사용자가 정의한 예외가 발생되었습니다")
    print(e)
    continue
  except Exception as e:
    print(e)
    continue
  finally:
    print("finally")
  break
print("프로그램 종료")  