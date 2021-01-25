from itertools import combinations

people = []

for _ in range(9):
    people.append(int(input()))

combList = list(combinations(people, 2))
for x, y in combList:
    result = sum(people) - x - y
    if result == 100:
        people.remove(x)
        people.remove(y)
        people.sort()
        break

for person in people:
    print(person)
