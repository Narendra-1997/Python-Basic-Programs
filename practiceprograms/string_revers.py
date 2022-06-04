# str="my name is narendra"
# l=[]
# m=str.split()
# for i in range(1,len(m)+1):
#     if i%2==0:
#         l.append(m[i-1][::-1])
#     else:
#         l.append(m[i-1])
# print(l)
# print("  ".join(l))


# s='hi iam narendra'
# l=[]
# s2=str()
# for i in s.split():
#     l.append(i[::-1])
# print(' '.join(l))


# s = "iam ram gopal and iam stupid"
# n = ''
# for i in s:
#     n = i + n
# print(n)
# p = ''
# for j in n.split():
#     # print(j)
#     p = j + " " + p
# print(p)
#
# from datetime import datetime

# def log_datetime(nani):
#     def wrapper():
#         # print(f'Function:{nani.__name__}\nRun on :{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
#         print("Run on:",datetime.today())
#         # print(f'{"-" * 30}')
#         nani()
#
#     return wrapper
#
#
# @log_datetime
# def daily_backup():
#     print('Daily backup job has finished')
#
#
# daily_backup()


from datetime import datetime


def login(dec):
    def inner_log():
        print(dec.__name__)
        print(f"my com backup ", datetime.today())
        dec()

    return inner_log


@login
def sample():
    print("how it has done")


sample()
