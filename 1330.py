from sys import stdin
#stdin = open("bakjoon/input.txt", "r")  # 테스트 파일을 읽을 때 사용합니다.

lines = []

for _ in range(1):
    lines.append(stdin.readline().rstrip())

tmp = lines[0]

[nbr1, nbr2] = map(int, tmp.split(' '))

if nbr1 > nbr2:
    print('>')
elif nbr1 < nbr2:
    print('<')
elif nbr1 == nbr2:
    print('==')