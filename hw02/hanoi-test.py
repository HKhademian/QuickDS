from hanoi import *

N=int(input('N: '))
S='A'
E='B'
T='C'

print('Start from:', S, 'to:', E, 'with help of:', T)
res = []

print('-' * 10)
print('<Normal> Hanoi: ')
res += [hanoi(N, S, E, T)]
print('moves:', res[-1])

print('-' * 10)
print('<A from|to B ban> Hanoi: ')
res += [hanoiXSE(N, S, E, T)]
print('moves:', res[-1])

print('-' * 10)
print('<S from|to T ban>  Hanoi: ')
res += [hanoiXST(N, S, E, T)]
print('moves:', res[-1])

print('-' * 10)
print('<E from|to T ban> Hanoi: ')
res += [hanoiXET(N, S, E, T)]
print('moves:', res[-1])


print('result moves:', res)
