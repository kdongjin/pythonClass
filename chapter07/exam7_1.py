# Quiz) "리그 오브 레전드" 게임에서 세명의 팀원이 얻은 골드량을 매개변수로 
# 받아, 팀의 평균 골드 획득량을 계산하는 함수 cal_average_gold를 정의하고 사
# 용해 보세요.
# cal_average_gold(12000, 15000, 18000)
# 실행결과
# 15000.0
# 그리고 가변인자를 받아서 실행하는 함수를 프로그램 해보세요.

def cal_average_gold(*no):
  avg = sum(no)/len(no)
  print(int(avg))


cal_average_gold(12000,15000,18000)