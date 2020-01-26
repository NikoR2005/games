import random

listx = []
listz = []
listy = []
listw = []

t1 = ("a", "b", "c")
t2 = ("d", "e", "f")
t12 = t1 + t2
t3 = [1, 2, 3, 4, 5]
t4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
c = len(listx) - 1
o = 0
numb = 0
'''
print(t12)
print(t1[1])
for elements in t12:
    t3.append(elements)
    t3.append('a')
print(t3)
print(t4)
t4.update({'a': t3[0], 'b': t3[1], 'c': t3[2], 'd': t3[3], 'e': t3[4], 'f': t3[5]})
print(t4)
if len(t3) - 1 == len(t4) - 1:
    print('same')
else:
    print('not same')

if len(t3) - 1 > len(t4) - 1:
    print('t3 has', len(t3) - 1 - len(t4) - 1, 'elements more than t4')

if len(t3) - 1 < len(t4) - 1:
    print('t4 has', len(t4) - 1 - len(t3) - 1, 'elements more than t3')

f5 = {'one': [4, 7, 6], 'two': [7, 8, 9, 9], 'three': [0, 9, 1], 'foor': [0, 9, 1]}


for key in f5.keys():
    biggest = sorted(f5.get(key), reverse=True)
    listz.append(key)
    listx.append(biggest[0])

listx.sort(reverse=True)

for key in f5.keys():
    biggest = sorted(f5.get(key), reverse=True)
    result[key] = biggest[0]

for key in result.keys():
    print(key, result[key])
print(result)

for key in result.keys():
    if len(resulta) > 0:
        if next(iter(resulta.values())) < result.get(key):
            resulta.clear()
            resulta[key] = result.get(key)
    if resulta.get(key) == result.get(key):
        resulta[key] = result.get(key)
    else:
        resulta[key] = result.get(key)

print(resulta)

f5 = {'one': [4, 7, 6], 'two': [7, 8, 9, 9], 'three': [10, 11, 12]}
result = {}

for key in f5.keys():
    biggest = sorted(f5.get(key), reverse=True)
    listz.append(key)
    listx.append(biggest[0])

listx.sort(reverse=True)

for key in f5.keys():
    biggest = sorted(f5.get(key), reverse=True)
    result[key] = biggest[0]

for key in result.keys():
    print(key, result[key])
print(result)
for key in result:


while c < len(f5) - 1:
    test = f51('one')
    for i in f51:
        if i < test:
            passed_test == True
            passed_number == passed_test
            print(passed_number)
            c = c + 1
for small in f5.keys():
    small_sorted = sorted(small.items(), key=lambda kv: kv[0])
    print(small_sorted)
    for key in f5.keys():
        key_sorted = sorted(key.items(), key=lambda kv: kv[1])
        print(key_sorted)
        if f5.get(key_sorted) > f5.get(small_sorted):
            passed_test = key_sorted
'''


f5 = {'one': {'one': [11112223, 7, 6], 'two': [7, 8, 9, 9]}, 'two': {'one': [4, 722, 6], 'two': [7, 8,111111, 9]}}
result = {}
for key in f5.keys():
    for kee in f5.get(key).keys():
        for i in f5.get(key).get(kee):
            biggest = sorted(f5.get(kee).get(i), reverse=True)
            result[kee] = biggest[0]

print(result)
