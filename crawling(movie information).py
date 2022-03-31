import requests
from bs4 import BeautifulSoup
from time import sleep
import os

res = requests.get("https://movie.naver.com/movie/running/current.nhn")
soup = BeautifulSoup(res.text, "html.parser")


def 제거(st):
    for i in "\t\r\n":
        st = st.replace(i, "")
    return st

영화 = []
for i in soup.select(".lst_dsc")[:10]:
    제목 = i.select_one("a").text
    등급 = i.select_one("span").text
    A = i.select('.num')
    평점 = A[0].text
    예매 = A[1].text
    참여 = i.select_one(".num2 > em").text
    B = i.select(".info_txt1 > dd")
    개요들 = B[0].text # 영화장르, 개봉날짜, 상영시간
    영화감독 = B[1].text # 영화감독
    C = 제거(개요들).split("|")
    장르 = C[0]
    상시 = C[1]
    날짜 = C[2]
    감독 = 제거(영화감독)
    영화.append([제목, 등급, 평점, 예매, 참여, 장르, 상시, 날짜, 감독])


# 영화는 영화정보들(리스트) 의 리스트

while True:
    # 영화목록 출력
 
    print("="*30)
    print("현재 상영중인 영화 TOP 10")
    print("="*30)

    num = 1
    for i in 영화:
        print(f"{num}. {i[0]}")
        num += 1

    user = input("영화 선택 (종료 q) : ")

    if user.isnumeric():
        user = int(user)
        if 1 <= user <= 10:
            선택영화 = 영화[user-1]

            print(f"\n\n{선택영화[0]} 선택!!!")
            sleep(0.7)
            os.system("cls")
            print("="*40)
            print(f"{선택영화[0]} INFORMATION!!")
            print("="*40)
            print(f"관람등급\t{선택영화[1]}")
            print(f"영화평점\t{선택영화[2]}")
            print(f"예매유울\t{선택영화[3]}")
            print(f"평점참여\t{선택영화[4]}")
            print(f"영화장르\t{선택영화[5]}")
            print(f"상영시간\t{선택영화[6]}")
            print(f"개봉날짜\t{선택영화[7]}")
            print(f"영화감독\t{선택영화[8]}")
            input("\n\n메인으로가기 (ENTER)")

        else: 
            print("1 에서 10 까지만 입력해주세요.")
    else:
        if user.lower() == 'q':
            print("프로그램 종료 :) ")
            break
        else:
            print("숫자 입력하시길 바랍니다!!!")

    sleep(0.7)
    os.system("cls")