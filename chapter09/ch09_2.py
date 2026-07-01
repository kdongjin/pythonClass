#자바상속( 부모것은 내것, 자식은 반드시 super(), 오버라이딩) 다중상속안됨(모호성)
#파이썬상속( 부모것은 내것, 자식은 반드시 부모.__init__(self, 매개변수)
# ,super(self 가 들어가지 않음), 오버라이딩) 다중상속됨(모호성 발생하지 않는다: 순서가 정해져있다.)

# 일반유닛(공격력이 없는 유닛)
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name}, 체력:{self.hp} 이동속도:{self.speed} 유닛이 생성되었습니다")

nurse1 = Unit("간호사1", 40, 5)   
nurse2 = Unit("간호사2", 40, 5)   

# 공격력이 있는 유닛(상속)
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, speed, damage):
    # 다중상속때 문제가 생김
    # 부모를 책임짐
    # super().__init__(name, hp, speed)
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  #멤버함수
  def attack(self, location):
    print(f"{self.name}이 현재체력: {self.hp}  {location}방향으로  {self.speed}로 공격력{self.damage} 공격중임.")

  # 상대방의 공격력을 받게되었을때 처리함수: damage
  def damaged(self, damage):
    print(f"{self.name}이 상대방의 공격{damage}을 받았습니다.")
    self.hp = self.hp - damage

    if self.hp <= 0: 
      print(f"{self.name}은 파괴되었습니다.")
    else:
      print(f"{self.name} 유닛은 체력이 {self.hp} 가 남아있습니다. ")

# 화염방사병: 공격유닛
fireSoldier = AttackUnit("화염방사병", 40, 10, 10)

# 화염방사병 공격명령(2시방향)
fireSoldier.attack("2시")

# 화염방사병이 공격을 받겠습니다.
fireSoldier.damaged(20)
fireSoldier.damaged(10)
fireSoldier.damaged(10)
