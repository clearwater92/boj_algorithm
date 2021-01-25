string = input()
stack = []
res = ''
temp = ''
isTag = False 

for letter in string:
	if letter == '<':
		isTag = True
		res += temp[::-1] + '<'
		temp = ''
	elif letter == '>':
		isTag = False
		res += '>'
	elif letter == ' ':
		if isTag:
			res += ' '
		else:
			res += temp[::-1] + ' '
			temp = ''
	else:
		if isTag:
			res += letter
		else:
			temp += letter
res += temp[::-1]
print(res)