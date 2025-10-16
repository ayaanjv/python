num = int(input())
space='  '
print('+',end='')
for i in range (num):
    print("-+")
    for j in range(i):
        print(space,end='')
    print('| |')
    for k in range(i):
        print(space,end='')
    print('+-+',end='')
print()
