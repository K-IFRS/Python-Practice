import random
win=0
lose=0

#삼세판 설정 및 가위바위보 입력
while win!=3 and lose!=3:
    com=random.randint(1,3)
    user=int(input("가위바위보를 선택하세요(1.가위, 2.바위, 3.보): "))
    print("===================================================")

#입력값 출력
    if user==1:
        print("당신의 선택은 (가위)입니다.")
    elif user==2:
        print("당신의 선택은 (바위)입니다.")
    elif user==3:
        print("당신의 선택은 (보)입니다.")

    if com==1:
        print("컴퓨터의 선택은 (가위)입니다")
    elif com==2:
        print("컴퓨터의 선택은 (바위)입니다.")
    elif com==3:
        print("컴퓨터의 선택은 (보)입니다.")

#승패 결정 및 출력
    승패=user-com

    if 승패==0:
        print(f"비겼습니다! 현재 스코어 {win}승 {lose}패")
        print("===================================================")
    elif 승패==-2 or 승패==1:
        win+=1
        print(f"이겼습니다! 현재 스코어 {win}승 {lose}패")
        print("===================================================")
    elif 승패==-1 or 승패==2:
        lose+=1
        print(f"졌습니다! 현재 스코어 {win}승 {lose}패")
        print("===================================================")

#최종 결과 출력         
if win==3:
    print("먼저 3승을 했네요. 최종 승리!")
else:
    print("컴퓨터가 먼저 3승을 했네요. 최종 패배!")
