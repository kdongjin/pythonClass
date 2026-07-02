# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 작성
# (모듈 사용 예제) 
# import byme
# byme.sign()
# (출력 예제)
# 이 프로그램은 홍길동에 의해 만들어졌습니다. 
# 홈페이지 : http://hongGilDong.com/
# 이메일 : hongGilDong@gmail.com

import byme

byme_obj = byme.Byme()
byme_obj.sign()