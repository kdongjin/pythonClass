# 딕셔너리(key, value)

# key값은 절대중복허용하지 않음. value값은 중복이 이루어져도 아무문제없다.
cabinet = {3:'푸',100:'피글렛',3:'수푸',4:'피글렛'}   #{3: '수푸', 100: '피글렛', 4: '피글렛'}
cabinet[5] ='쿠우'    #추가 {3: '수푸', 100: '피글렛', 4: '피글렛', 5: '쿠우'}
# del cabinet[5]        #삭제 {3: '수푸', 100: '피글렛', 4: '피글렛'}
# cabinet[4] = '피클렛2' #수정 {3: '수푸', 100: '피글렛', 4: '피클렛2'}
# print( 3 in cabinet)   # 키값이 존재하면 True
# print(cabinet)

# 주의 dictionary에서 value in 으로 체크가 안된다. 
# print( '피글넷' in cabinet)  #False  {3: '수푸', 100: '피글렛', 4: '피클렛2'}

# key값 value값  items(키값, value값 모두가져옴)가져오는방법
# cabinet = {100:'피글렛',3:'수푸',4:'피글렛2'} 
# print(cabinet.keys())    #dict_keys([100, 3, 4])
# print(cabinet.values())  #dict_values(['피글렛', '수푸', '피글렛2'])
# print(cabinet.items())  #dict_items([(100,'피글렛'), (3,'수푸'), (4,'피글렛2')])

# for문을 출력하시오. (키값 => 조회해서 벨류값 출력)
cabinet = {100:'피글렛',3:'수푸',4:'피글렛2'} 

# keyList = cabinet.keys()      #dict_keys([100, 3, 4])
# for  key  in keyList:
#   print(cabinet[key])

# 전체삭제하는기능
cabinet = {100:'피글렛',3:'수푸',4:'피글렛2'} 
cabinet.clear()         # { }
print(cabinet)  