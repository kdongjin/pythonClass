#  반복문

# 반복문1
list = [1,3,5,7,9]
for no in list:
  print("{}".format(no), end=" ")
print("")

# 반복문2 
for no in [1,3,5,7,9]:
  print("{}".format(no), end=" ")
print("")

# 반복문3 
for no in range(10,0,-2):
  print("{}".format(no), end=" ")
print("")

# 반목문4
orders = ["햄버거", "짜장면", "짬봉"]
for data in orders:
  print("{}".format(data), end=" ")


# 반목문5 (한줄 for문(list comprehension))
print("")
students = [1,2,3,4,5]
print(students)
#students = [11,12,13,14,15] #변경되기를 희망
students = [ no * 10 + 100 for no in students  ]
print(students)

menu = ["햄버거", "짜장면", "짬봉"]
print(menu)
menu1 = [ len(data)  for data  in  menu]
print(menu)
print(menu1)

like_subject =["java","python", "html", "javascript", "spring boot"]
like_subject = [ subject.upper() for subject  in like_subject ]
print(like_subject)

# 반복문 6
count = 0
exitFlag = False
while not exitFlag:
  count += 1
  print("count = {}".format(count))
  if count >= 100:
    exitFlag = True

# 반목문 7  변수 in  [ list구조] 

data_list = [1,2,3,4,5]
no = int(input("[1,2,3,4,5] 선택입력>>"))

# for i  in data_list:
#   if no == i :
#     print( "있어요")
#     break
#   else:
#     print("없어요")

if no in data_list:
  print( "있어요")
else:
  print( "없어요")

  
