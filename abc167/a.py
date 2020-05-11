S = input()
T = input()

sl = len(S)
tl = len(T)

if sl == tl-1 and S == T[:tl-1]:
    print("Yes")
else:
    print("No")