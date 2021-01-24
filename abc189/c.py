from collections import deque

N = int(input())
A = list(map(int,input().split()))

def rectangle(n, hs): #n:横　hs: ヒストグラム
    stack = deque() # stack = (j, h) 位置と高さが格納される
    ans = 0
    for i, h in enumerate(hs):
        j = -1
        while stack and stack[-1][1] > h:
            j, h2 = stack.pop()
            ans = max(ans, (i-j) * h2)
            
        if not stack or stack[-1][1] < h: #stackが空、もしくはstackのトップにある"高さh"が、ヒストグラムの高さよりも小さければ、候補としてstackに追加。
            stack.append( (i if j == -1 else j, h))
        
    ans = max(ans, max((n-j) * h2 for j, h2 in stack))
    
    return ans

ans = rectangle(N,A)

print(ans)