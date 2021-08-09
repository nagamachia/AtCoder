X=input()

if int(X)%1111==0:
    print("Weak")
elif X[1]==str(int(X[0])+1)[-1] and X[2]==str(int(X[1])+1)[-1] and X[3]==str(int(X[2])+1)[-1]:
    print("Weak")
else:
    print("Strong")