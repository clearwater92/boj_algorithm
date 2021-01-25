# 문자열 처리 이용하여 풀기 600ms
# tc = int(input())
# for _ in range(tc):
# 	word = input()
# 	wordArr = word.split()
# 	result = ''
# 	for letter in wordArr:
# 		result += letter[::-1]
# 		result += ' '
# 	result.rstrip()
# 	print(result)

#스택 이용하여 풀기 664ms
N = int(input())
# N = int(sys.stdin.readline())
for _ in range(N):
    stack = []
    result = ''
    line = input()
    for char in line:
        if char == ' ':
            while stack:
                result += stack.pop()
            result += ' '
        else:    
            stack.append(char)
    while stack:
        result += stack.pop()
    print(result)

#참고
#https://bbunada.tistory.com/34