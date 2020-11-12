t = int(input())
for i in range(t):
    n = int(input())
    for j in range(2*n + 2, 4*n + 1, 2):
        print(j, end=" ")
    print()