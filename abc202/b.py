S=input()

S=list(reversed(S))

for i in range(len(S)):
    if S[i]=="6":
        S[i]="9"
    elif S[i]=="9":
        S[i]="6"

print("".join(S))