from sys import stdin
#stdin = open("bakjoon/input.txt", "r")  # 테스트 파일을 읽을 때 사용합니다.

lines = []

for _ in range(2):
    lines.append(stdin.readline().rstrip())

word = lines[0]

print(word[int(lines[1]) - 1])