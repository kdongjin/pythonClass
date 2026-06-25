# Quiz) 여러 회사의 주식 가격이 회사별로 딕셔너리에 리스트로 저장되어 있다. 각 
# 회사별 주식 가격의 평균을 계산하는 프로그램을 작성하세요.
# stock_prices = {
# '삼성전자': [81000, 81500, 82000],
# 'SK하이닉스': [140000, 141000, 139500],
# '네이버': [350000, 355000, 345000]
# }
# 실행결과
# # 삼성전자 평균 주식 가격: 81500
# # SK하이닉스 평균 주식 가격: 140166 
# # 네이버 평균 주식 가격: 350000
stock_prices = {
'삼성전자': [81000, 81500, 82000],
'SK하이닉스': [140000, 141000, 139500],
'네이버': [350000, 355000, 345000]
}

keyList = stock_prices.keys()

for key  in keyList:
  value = stock_prices[key]
  total = 0
  for data  in value:
    total = total + data
  # print("{} 평균 주식 가격: {}".format(key, round(sum(value)/len(value),2)))
  print("{} 평균 주식 가격: {}".format(key, round(total/len(value),2)))


# for key, value in  stock_prices.items():
#   print(key,"평균주식가격" , round(sum(value)/len(value),2))
