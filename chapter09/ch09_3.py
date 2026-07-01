# 다중상속 진행한다. (모호성을 해결하는 방법을 구현한다.

# 일반유닛(지상 공격력이 없는 유닛)
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name}, 체력:{self.hp} 이동속도:{self.speed} 유닛이 생성되었습니다")

  def move(self, location):
    print(f"{self.name} 지상유닛이 {location} 방향으로 가고 있습니다.")


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


# 공중 유무 유닛(공중에서 업무 진행할 수 있는 체크)
class Flyable:
  def __init__(self, flying_speed):
     self.flying_speed = flying_speed

  # 멤버함수
  def fly(self, name,  location):
    print(f"{name} 유닛이 {self.flying_speed}로 {location} 방향으로 날아가고 있습니다.")


# 다중상속 (지상공격유닛, 공중유무 유닛)
# AttackUnit(name, hp, speed, damage), Flyable(flying_speed))
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, speed, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, speed, damage)
    Flyable.__init__(self, flying_speed)
  
  #오버라이딩
  def move(self, location):
    print(f"{self.name} 공중유닛이 {location} 방향으로  {self.flying_speed}속도 날아가고 있습니다.")


# 공격기능을 가진 interceptor 객체생성

intercepter = FlyableAttackUnit("요격기", 300, 0, 80, 200)
# intercepter.attack("2시방향")
# intercepter.damaged(60)
# intercepter.fly(intercepter.name, "4시")
intercepter.move("3시")