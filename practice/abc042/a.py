A,B,C = map(int, input().split())
ABC = [A,B,C]
# print(sorted(ABC))
if sorted(ABC) == [5,5,7]:
    print("YES")
else:
    print("NO")