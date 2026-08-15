for i in range(1, 21):  
    for j in range(1, 21 - i + 1):
        if j == 1 or j == 21 - i or i == 20:
            print("*", end="")
        else:
            print(" ", end="")
    print()