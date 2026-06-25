# 자료구조의 변경

# set => list 변경
menu = {"햄버거", "콜라", "감자튀김"}
print(menu, type(menu))   #{'햄버거', '감자튀김', '콜라'} <class 'set'>
menu = list(menu)
print(menu, type(menu))   #['감자튀김', '콜라', '햄버거'] <class 'list'>

# list => tuple
menu = tuple(menu)
print(menu, type(menu))   #('감자튀김', '콜라', '햄버거') <class 'tuple'>

# tuple => set
menu2 = ('감자튀김', '콜라', '햄버거','햄버거')
print(menu2)  # ('감자튀김', '콜라', '햄버거','햄버거')
menu2 = set(menu2)
print(menu2, type(menu2))   #{'감자튀김', '콜라', '햄버거'} <class 'set'>