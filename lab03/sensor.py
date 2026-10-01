porog = float(input())
n = int(input())
cheter = 0
pr = 0
maxn = -100
s = 0
srz = 0
orc = 0
for i in range(n):
    new = input()
    if new == 'error':
        cheter += 1
    else:
        neer = float(new)
        if neer > porog:
            pr += 1
        if neer > maxn:
            maxn = neer
        srz += neer
        orc += 1
srz /= orc
print('Всего записей: ',n)
print('Кол-во ошибок: ', cheter)
print('Кол-во превышений: ', pr)
print('Макс показание', f'{maxn:.1f}')
print('Ср. показание: ', f'{srz:.1f}')
#ааа
