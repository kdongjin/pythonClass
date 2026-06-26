# 피클 (pickle)

import pickle

#pickle 파일저장
# binary 파일로 저장할때에는 encoding 방식이 필요핮 않음.

# profile_handle = open("profile.pickle", "wb")
# profile_dic = {"이름":"kdj", "나이": 62, "취미": ["등산","배드민턴","탁구"]}
# #dump: 우리가 프로그램에서 사용했던, 맵구조(dictionary) 다시 사용하기 위해서 pickle 파일에 저장
# pickle.dump(profile_dic, profile_handle)
# profile_handle.close()

# pickle 파일을 다시 가졍와서 프로그램 사용하기 위한 기능
# profile_handle = open("profile.pickle", "rb")
# list_dic = pickle.load(profile_handle)
# profile_handle.close()

# for key, value in  list_dic.items() :
#   print(key, value)


# 파일을 한번에 열고, 자동을 닫기: with문 (자바: try with resources)
# with open("profile.pickle", "rb") as profile_handle:
#   list_dic = pickle.load(profile_handle)
#   for key, value   in list_dic.items() : 
#     print(key, value)
#     if key == "취미":
#       for  data in  value:
#         print("{} = {}".format(key, data))

# print("with  profile_handle.close() 안해도 된다.")


# 일반파일을 with 처리하는방식 (닫는기능 자동으로 처리)
# with open("data.txt", "w", encoding="utf-8") as data_handle:
#   data_handle.write("파이썬\n")
#   data_handle.write("자바\n")
#   data_handle.write("스프링부트\n")


with open("data.txt", "r", encoding="utf-8") as data_handle:
  print(data_handle.read())