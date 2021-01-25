e, s, m = map(int, input().split())
year = 0
esm = [0, 0, 0]
while esm[0] != e or esm[1] != s or esm[2] != m:
    year += 1
    esm[0] += 1
    esm[1] += 1
    esm[2] += 1
    if esm[0] == 16:
        esm[0] = 1
    if esm[1] == 29:
        esm[1] = 1
    if esm[2] == 20:
        esm[2] = 1

print(year)