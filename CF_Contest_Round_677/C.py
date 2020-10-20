def problem_sol(x, n):
    maximum = max(x)
    found = False
    if all(i == maximum for i in x):
        found = True
        print(-1)
    else:
        if x[0] == maximum:
            if x[1] < maximum:
                found = True
                print(1)
        if x[n - 1] == maximum and not found:
            if x[n - 2] < maximum:
                found = True
                print(n)
        if not found:
            for i in range(1, n - 1):
                if x[i] == maximum:
                    if x[i - 1] < maximum or x[i + 1] < maximum:
                        found = True
                        print(i + 1)
                        break
    if not found:
        print(-1)


no_inp = int(input())
while no_inp > 0:
    n = int(input())
    x = list(map(int, input().split()))
    problem_sol(x, n)
    no_inp -= 1
