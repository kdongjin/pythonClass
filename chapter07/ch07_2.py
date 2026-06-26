# 전역변수, 지역변수

#카센터 데이터 총갯수

#전역변수
car_total = 100

def rent(rent_count):
  #전역변수를 사용하기 위해서는 [ global 변수 ]
  global car_total
  car_total = 200
  if car_total > rent_count :
    car_total = car_total - rent_count
    print("랜트할 {}대 진행합니다. 차 남는 갯수 {}입니다.".format(rent_count,car_total))
  else:
    print("죄송합니다. 랜트할 차가 없습니다.")

rent(10)
print(car_total)