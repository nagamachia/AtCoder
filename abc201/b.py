N=int(input())

ST_dict={}
ST=[]

for i in range(N):
    st = input().split()
    ST.append(int(st[1]))
    ST_dict[int(st[1])]=st[0]

ST_sorted = sorted(ST,reverse=True)

print(ST_dict[ST_sorted[1]])


