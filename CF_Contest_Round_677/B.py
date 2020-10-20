def problem_sol(x, n):
    l = n
    first = -1
    last = 0
    zeros_safe = 0
    zeros_unsafe = 0
    for i in range(0, l):
        if x[i] == 1 and first == -1:
            first = i
        if first != -1:
            if x[i] == 0:
                zeros_unsafe += 1
            if x[i] == 1:
                zeros_safe = zeros_unsafe
    print(zeros_safe)


no_inp = int(input())
while no_inp > 0:
    n = int(input())
    x = list(map(int, input().split()))
    problem_sol(x, n)
    no_inp -= 1
