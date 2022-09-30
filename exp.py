
from asyncio.windows_events import NULL




# [varx[1] for varx in enumerate(vara) if varx[0] in a]


l = []
# print([i for i in vara])
# print(len(vara))

a = ["22","3"]
rule = ('4','22')

for i in a:
    for j in rule:
        if i == j:
            # you can take i or j value both are same
            print(i)
            l.append(tuple(i))
        else:
            print(None)


print(l)