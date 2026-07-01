# 클래스 (멤버변수, 생성자, 멤버함수(겟터,셋터, 오버로딩, 오버라이딩, 기능))
# 클래스 (멤버변수(public), 생성자, 멤버함수(오버로딩, 오버라이딩, 기능))
# 클래스 Unit, 멤버변수(정적,인스멤): 이름, 체력, 공격력, 이동스피드

class Unit:
  
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print(f"{self.name} 유닛이 생성되었습니다")
    print(f"체력 :{self.hp} 공격력: {self.damage}")

# Unit 객체를 생성한다. 병사2, 탱크 객체를 생성한다.
# soldier1 = Unit("보병1", 40, 5)
# soldier2 = Unit("보병2", 40, 5)
# tank = Unit("탱크1", 150, 20)

# 해당된 객체에서 멤버변수가 필요하면 , 동적할당할 수 있다. 
# 그러나 다른 객체에는 영향을 미치지 않는다.  
# tank.fly = False
#print(f"{tank.name}  {tank.hp}  {tank.damage}  {tank.fly}")
#print(f"{soldier1.name}  {soldier1.hp}  {soldier1.damage}  {soldier1.fly}")


#  클래스 메소드기능(공격하는 기능: attack, 공격을 당하는 기능: damaged)
class AttackUnit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print(f"{self.name} 유닛이 생성되었습니다")
    print(f"체력 :{self.hp} 공격력: {self.damage}")

  def attack(self, location):
    print(f"{self.name}이 현재체력: {self.hp}  {location}방향으로  공격력{self.damage} 공격중임.")

  # 상대방의 공격력을 받게되었을때 처리함수: damage
  def damaged(self, damage):
    print(f"{self.name}이 상대방의 공격{damage}을 받았습니다.")
    self.hp = self.hp - damage

    if self.hp <= 0: 
      print(f"{self.name}은 파괴되었습니다.")
    else:
      print(f"{self.name} 유닛은 체력이 {self.hp} 가 남아있습니다. ")

# 화염방사병: 공격유닛
fireSoldier = AttackUnit("화염방사병", 40, 10)

# 화염방사병 공격명령(2시방향)
fireSoldier.attack("2시")

# 화염방사병이 공격을 받겠습니다.
fireSoldier.damaged(20)
fireSoldier.damaged(10)
fireSoldier.damaged(10)
