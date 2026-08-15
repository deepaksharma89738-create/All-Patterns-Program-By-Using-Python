for i in range(1, 21):
    for j in range(1, 21):
        if i == 1 or i == 20 or j == 1 or j == 20:
            print("*", end="")
        else:
            print(" ", end="")
    print()