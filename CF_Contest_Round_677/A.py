def problem_sol(x):
    s = 0
    found = False
    for i in range(1, 10):
        if found:
            break
        for j in range(1, 5):
            if j * str(i) == str(x):
                s += j
                found = True
                break
            else:
                s += j
    print(s)

asd
no_inp = int(input())
while no_inp > 0:
    x = int(input())
    problem_sol(x)
    no_inp -= 1
