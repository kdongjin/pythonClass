# 외부 패키지를 다운로드 설치하는 방법 
# https://pypi.org/  현재 (80만개 패키지 들어있음)
# pip install beautifulsoup4
# 해당되는 패키지에 사용하는 방법들이 설명되어 있다.(Read.me)

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 우리가 필요한 텍스트를 찾는다.
print(soup.find(string="bad1"))

find_str = input("찾고자 하는 단어 >>")
if soup.find(string=find_str) :
  print("원하는 데이터를 찾았습니다.")
else:
  print("원하는 데이터는 없습니다")

print(soup.p)  