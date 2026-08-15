for i in range(1, 21):
    for j in range(1, 21 - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == 20:
            print("*", end="")
        else:
            print(" ", end="")
    print()