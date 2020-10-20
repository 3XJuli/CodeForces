no_inp = int(input())


def problem_sol(a, b):
    sol = 0
    bin_a, bin_b = map(str, [bin(a), bin(b)])
    bin_a = bin_a[2:]
    bin_b = bin_b[2:]
    len_diff = len(bin_a) - len(bin_b)
    if len_diff < 0:
        bin_a = '0' * (-len_diff) + bin_a
    elif len_diff > 0:
        bin_b = '0' * len_diff + bin_b
    for i, c in enumerate(bin_a):
        if bin_a[i] != bin_b[i]:
            sol += 2 ** (len(bin_a) - 1 - i)
    print(sol)


while no_inp > 0:
    a, b = map(int, input().split())
    problem_sol(a, b)
    no_inp -= 1
