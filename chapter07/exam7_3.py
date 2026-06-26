# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식) 
# 남자 : 키(m) x 키(m) x 22 
# 여자 : 키(m) x 키(m) x 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender) 
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제) 
# 키 175cm 남자의 표준 체중은 67.38kg 입니다

def std_weight(height, gender):
  if(gender == "남자" or gender == "남"):
    return height * height * 22
  elif(gender == "여자" or gender == "여"):
    return height * height * 21
  else:
    return 0

height = float(input("키를 입력해주세요(170cm):")) 
gender = input("성별을 입력해주세요(남자/여자) : ")

# 174cm => 1.74m 변경 
cal_height = height/100

weight = std_weight(cal_height, gender)

if(weight != 0):
  print("키 {} {}의 표준체중은 {}kg입니다.".format(int(height),gender,round(weight,2)))
else:
  print("잘못된 성별 입력입니다.")