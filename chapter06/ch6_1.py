# if문

# "아파요"
# message = input("당신몸상태는(아파요/좋아요)>>")
# if message == "좋아요" :
#   print("몸상태가 좋으니 놀러가요")
# else:
#   print("몸상태가 좋지않으니 집에서 휴식해요")

# 점수입력을 받아서 등급을 표시하는 프로그램(A,B,C,D,F)
# score = int(input("당신의 수학점수는>>"))
# print(score, type(score))

# grade = "F"
# if score >= 90 :
#   grade = "A"
# elif 80 <= score < 90 :
#   grade = "B"
# elif 70 <= score < 80 :
#   grade = "C"
# elif 60 <= score < 70 :
#   grade = "D"  
# else:
#   grade = "F"
# print(f"당신점수는 {score}점입니다. {grade}등급입니다. ")

# 파이썬 3.10 이상 사용가능함.(자바 :switch case, match case)
# score = int(input("당신의 수학점수는>>"))
# match score // 10:
#   case 10 | 9: 
#     grade = "A"
#   case 8:
#     grade = "B"
#   case 7:
#     grade = "C"
#   case 6:
#     grade = "D"
#   case _:
#     grade = "F"
# print(f"당신점수는 {score}점입니다. {grade}등급입니다. ")

# match case 확장기능
score = int(input("당신의 수학점수는>>"))
match score:
  case _ if 90<= score <= 100: 
    grade = "A"
  case _ if 80<= score < 90:
    grade = "B"
  case _ if 70<= score < 80:
    grade = "C"
  case _ if 60<= score < 70:
    grade = "D"
  case _:
    grade = "F"
print(f"당신점수는 {score}점입니다. {grade}등급입니다. ")




