n = input()
output_list = []
input_list = []
for el in n:
	output_list.append(el)

cursor = len(n)
m = int(input())

for i in range(m):
	input_list.append(input())
	if input_list[0] == 'L' and output_list:
		input_list.popleft()
	elif input_list[0] == 'D' and (len(arr) - 1) >= cursor:
		cursor -= 1 

for ip in input_list:
	if ip == 'L':
		if cursor > 0:
			cursor-=1
	elif ip == 'D':
		if cursor <= len(output_list) - 1:
			cursor+=1
	elif ip == 'B':
		if cursor > 0:
			cursor-=1
			output_list.pop(cursor)
	else:
		output_list.insert(cursor, ip[2])
		cursor+=1
print(''.join(arr))