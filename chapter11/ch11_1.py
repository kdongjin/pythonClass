# 내부모듈을 가져와서 사용하기 

# import theater_module

# # #일반인 영화예매 3명
# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_soldier(3)

# 가져온 모듈 별칭
# import theater_module as tm
# tm.price(3)
# tm.price_morning(3)
# tm.price_soldier(3)

# 가져온 모듈 별칭없이 바로 사용
# from  theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# 가져온 모듈 별칭없이 바로 price , price_morning 이것만 사용
# from  theater_module import price , price_morning
# price(3)
# price_morning(3)
# price_soldier(3)   # price_soldier(3) import가 안되서 사용할 수 없음.


# 가져온 모듈 별칭없이 바로 price 이것만 사용(별칭을 이용해서 사용가능)
from  theater_module import price as p
p(3)
