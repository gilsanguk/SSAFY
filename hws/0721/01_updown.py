import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
    print(answer)
    # 여기부터 코드를 작성하세요.
    while True:
        N=int(input('1이상 10000이하의 숫자를 입력하세요. : '))
        if N < 1 or N > 10000:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            continue
        elif answer == N:
            print(f'Correct!!! {counts}회 만에 정답을 맞췄습니다.\n')
            yes_or_yes = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. : ')
            if yes_or_yes == 'y':
                continue
            elif yes_or_yes == 'n':
                print('이용해주셔서 감사합니다. 게임을 종료합니다.')
                break
            else:
                print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
                break
        elif answer > N:
            print('Up!!!')
            counts +=1
        elif answer < N:
            print('Down!!!')
            counts +=1