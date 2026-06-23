# 문자열에서 자주사용하는방법 : slicing [], find() , count(), replace() 

# 문자열  """ ~~~ """  ''' ~~~ ''': 여백,또는 공백 기능까지 모두포함해서 문자열취급한다.  ***

# message = "파이썬을 공부하고 있습니다."
# print(message, type(message))

# message2 = '''
# 파이선을
# 공부
# 하고 있습니다.
# '''
# print(message2, type(message2))

# 슬라이싱  []

jumin = "990829-1550823"

# print("사용자 성별번호 :", jumin[7])
# print("사용자  연도 :", jumin[0:2])
# print("사용자  월 :", jumin[2:4])
# print("사용자  일 :", jumin[4:6])
# print("사용자  생년월일 :", jumin[0:6])
# print("사용자  생년월일 :", jumin[:6])
# print("주민번호뒷자리 :", jumin[7:])
# print("주민번호뒷자리 :", jumin[-7:])
# print("주민번호뒷자리 검증번호이전 :", jumin[7:-1])
# print("주민번호 문자열 길이 :", len(jumin))

# 반복문을 이용해서 주민번호 한자리씩을 출력하시오. '-' 생략하시오.

# for i in range(0, len(jumin)):
#   if jumin[i] == "-" :
#     continue
#   print(jumin[i], end=" ")

# 문자열 처리함수

# message = "Python is Amazing"

# print(message.lower())  #python is amazing
# print(message.upper())  #PYTHON IS AMAZING
# print(message.isupper())  #False
# print(message[0].isupper())  #True
# print(message[1:3].islower())  #True
# # replace   *** 문자열에서 필용한 영역을 다른글로 교체가 가능(자바 이런기능을 사용할려면 많은 메모리가 사용됨)
# print(message.replace("Python", "java"))  #True


# find , index 차이점을 체크
# find 진행에서 찾는것이 없으면  -1, 다음문장으로 실행한다.
# index 진행에서 찾는것이 없으면  ValueError 발생시키고, 다음문장으로 실행하지 않는다. 
# index 개념보다는 find를 사용하는것이 좋다.  ***

# message = "Python is Amazing"
# findIndex = message.find("n")
# print(findIndex)   # 5

# findIndex2 = message.find("n", findIndex+1)
# print(findIndex2)   # 15

# findIndex3 = message.find("is")
# print(findIndex3)  # 7

# findIndex4 = message.find("kim") # 찾지 못하면 -1 값을 리턴하고 다음문장을 실행한다.
# print(findIndex4)  # -1
# print("hello")

# findIndex6 = message.find("n", 6, -1)
# print(findIndex6)



message = "Python is Amazing"
# findIndex = message.index("n")
# print(findIndex)   # 5

# findIndex2 = message.index("n", findIndex+1)
# print(findIndex2)   # 15

# findIndex3 = message.index("is")
# print(findIndex3)  # 7

# findIndex5 = message.index("n", 6, -1)
# print(findIndex5)

# findIndex4 = message.index("kim")  # 찾지 못하면 ValueError 발생이되서 그 위치 멈추고 다음문장을 실행하지 않음
# print(findIndex4)  # -1
# print("Hello")



message = "Python is Amazing"
# print(message.count("n"))  # 2
# print(message.count("k"))  # 0
# print(len(message))  # 17


# 문자열포맷

# print("java"+"python")  #javapython
# print("java","python")  #java python

# age = 20
# print("나는 %d살입니다."%age)
# like = "파이썬"
# print("나는 %s을 좋아합니다."%like)
# grade = "A"
# print("java언어의 점수는 %c 등급입니다."%grade)
# score = 96.50
# print("java언어의 점수는 %.2f 입니다."%score)
# flag = True
# print("나는 java언어를 좋아하는것은 %s 입니다."%flag)
# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 %s과 %s입니다."%(fruit1,fruit2))

# 선호하는 방법
# age = 20
# print("나는 {}살입니다.".format(age))
# like = "파이썬"
# print("나는 {}을 좋아합니다.".format(like))
# grade = "A"
# print("java언어의 점수는 {}등급입니다.".format(grade))
# score = 96.50
# print("java언어의 점수는 {} 입니다.".format(score))
# flag = True
# print("나는 java언어를 좋아하는것은 {0}입니다.".format(flag))
# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 {0}과 {1}입니다.".format(fruit1, fruit2))
# print("나는 좋아하는 과일은 {1}과 {0}입니다.".format(fruit1, fruit2))

# 선호하는 방법
# age = 20
# print(f"나는 {age}살입니다.")
# like = "파이썬"
# print(f"나는 {like}을 좋아합니다.")
# grade = "A"
# print(f"java언어의 점수는 {grade}등급입니다.")
# score = 96.50
# print(f"java언어의 점수는 {score} 입니다.")
# flag = True
# print(f"나는 java언어를 좋아하는것은 {flag}입니다.")
# fruit1 = "수박"
# fruit2 = "참외"
# print(f"나는 좋아하는 과일은 {fruit1}과 {fruit2}입니다.")

# 탈출문자  \n  \t  \b  \r  \'  \"
print("파이썬\n자바")
print("파이썬\t자바")
print("파이썬\b자바")
print("파이썬\r자바")
print("파이썬보다 \"자바\"가 더 좋아요")
print('파이썬보다 \'자바\'가 더 좋아요')
print("D:\\JAVA_text\\nmetadata\\.mylyn")
















