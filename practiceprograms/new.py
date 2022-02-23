# l = []
# l2 = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
# print(','.join(l))


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


print(fact(8))
