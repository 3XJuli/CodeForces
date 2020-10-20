t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    k = l[0]
    if max(l) == min(l):
        print("NO")
    else:
        print("YES")
        for i in range(1, n):
            if (l[i] == k):
                l[i] = 0
            else:
                d = i
                print(1, i + 1)
        for i in range(n):
            if (l[i] == 0):
                print(d + 1, i + 1)
