# 집합(set)
# 중복을 허용하지 않는다.
my_set = {1,2,3,4,3,3}    # {1, 2, 3, 4}
my_set2 = {2,3,4,5,6}

print(my_set)         #{1, 2, 3, 4}
print(my_set2)        #{2, 3, 4, 5, 6}
# 두개의 set를 합집합
print(my_set | my_set2)  #{1, 2, 3, 4, 5, 6}
print(my_set.union(my_set2))

# 두개의 set를 교집합
print(my_set & my_set2)  #{2, 3, 4}
print(my_set.intersection(my_set2))  #{2, 3, 4}

# 두개의 set를 차집합
print(my_set - my_set2)  #{1}
print(my_set.difference(my_set2))  #{1}

#추가기능
my_set3 = {1,2,3,4}
my_set3.add(5)   #{1, 2, 3, 4, 5}
print(my_set3)   

#삭제기능
my_set4 = {"도라지","꿀","마늘","생강"}
my_set4.remove("도라지")
print(my_set4)  
