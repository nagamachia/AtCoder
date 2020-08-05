K = int(input())

# def is_prime(num):
#     # 2以外の偶数は素数ではないので無視する
#     if num % 2 == 0 and num != 2:
#         return False
    
#     # 繰り返しの上限を半分にする
#     for divisor in range(2, num//2):
#         if num % divisor == 0:
#             return False
            
#     return True

if K%2==0 or K%5==0:
    print(-1)
    exit()

if K==1:
    print(1)
    exit()
# if is_prime(K) and K%3!=0:
#     print(K-1)
#     exit()
if K%7==0:
    for i in range(1,K//7):
        if (pow(10,i,K//7)-1)/9%(K//7)==0:
            print(i)
            exit()
    print(-1)
    exit()

for i in range(1,K):
    if 7*(pow(10,i)-1)/9%K==0:
        print(i)
        exit()

print(-1)
