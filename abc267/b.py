S = input()

if S[0] == "1":
    print("No")
else:
    s = S[6]+S[3]+str(int(S[1]) or int(S[7]))+S[4]+str(int(S[2]) or int(S[8]))+S[5]+S[9]
    # print("s:",s)
    if ("101" in s) or ("1001" in s) or ("10001" in s) or ("100001" in s) or ("1000001" in s):
        print("Yes")
    else:
        print("No")