# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제) 총 3대의 매물이 있습니다. 
# 강남 아파트 매매 40억 2010년 
# 마포 오피스텔 전세 5억 2007년 
# 송파 빌라 월세 500/50 2000년
# [코드]
class House: 
  # 매물 초기화 
  def __init__(self, location, house_type, deal_type, price, completion_year): 
    self.location = location
    self.house_type = house_type
    self.dela_type = deal_type
    self.price = price
    self.completion_year = completion_year

  # 매물 정보 표시
  def show_detail(self):
    print(f"{self.location} {self.house_type} {self.dela_type} {self.price} {self.completion_year}년")

#  3개의 객체를 만든다.
house1 = House("강남", "아파트", "매매", "40억", 2010 )
house2 = House("마포", "오피스텔", "전세", "5억", 2007)
house3 = House("송파", "빌라", "월세", "500/50", 2000)

# 리스트를 만들어서 추가한다.
list = []
list.append(house1)
list.append(house2)
list.append(house3)

# 리스트 출력
print(f"총 {len(list)}대의 매물이 있습니다. ")
for h   in list:
  h.show_detail()