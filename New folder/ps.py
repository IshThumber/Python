# n = int(input())
# numb = input()
# lis = list(map(int, numb.split()))
# big, sbig = -6000, -6000
# for i in lis:
#     if (i > big):
#         big, sbig = i, big
#     elif (i < big and i > sbig):
#         sbig = i
# print (sbig)


n=input()
a=map(int,input().split())
a=list(set(a))
a.remove(max(a))
print (max(a))