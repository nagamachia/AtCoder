H1,M1,H2,M2,K = map(int, input().split())

ans = H2*60+M2-H1*60-M1-K

print(ans)