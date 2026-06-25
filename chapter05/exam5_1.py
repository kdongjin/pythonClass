# Quiz) 게임에서 플레이어가 얻은 점수들을 가진 scores 리스트가 있다. 가장 높은 점
# 수를 찾는 프로그램을 작성해 보세요. 
#  scores = [120, 150, 180, 200, 170] 
#
# 힌트) max_score 변수를 하나 생성해 준다.
# 실행결과
# 최고점수 : 200

# scores = [120, 150, 180, 200, 170]
# max_score = scores[0]

# for score  in  scores:
#   if max_score < score:
#     max_score = score

# print(f"{scores} \n최고값은:{max_score}")


# Quiz)게임에서 각 방에 숨겨진 아이템 개수를 나타내는 2차원 리스트가 있다. 모든 
# 방을 돌아다니며 아이템을 수집하는 프로그램을 작성하세요. 
# 아이템이 없는 방은 0 으로 표시된다.

# rooms = [ [3, 1, 2], [2, 0, 1], [1, 3, 2] ] 
# 힌트) sum(리스트)는 리스트의 합계를 계산해 준다.
# for room in rooms:
# total += sum(room)

rooms = [ [3, 1, 2], [2, 0, 1, 4, 5], [1, 3, 2] ]
total = 0

for room  in rooms:
  for  data in room:
    total = total + data

print("{}의 총합은 {}".format(rooms, total))

# for  room  in  rooms:
#   total = total + sum(room)
#   print(f"{room}의 합은 {sum(room)}")

# print(f"{rooms }의 총합은 {total}")