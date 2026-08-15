for i in range(1, 21):
    for j in range(1, 21 - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print(k, end="")
    print()