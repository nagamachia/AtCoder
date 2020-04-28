import pandas as pd
N, M = map(int, input().split())

if M == 0:
    print('0 0')
else:
    S = []
    for _ in range(M):
        S.append(input().split())
    
    df = pd.DataFrame(S,columns=['P','S'])
    ACdf = df[df['S'] == 'AC'].drop_duplicates()
    AC = len(ACdf)
    last = ACdf.tail(1).index.values[0]
    WAdf = df[(df[df['P'].isin(ACdf['P'])]['S'] == 'WA')][:(last-1)]
    WA = len(WAdf)
    print(AC, WA)
