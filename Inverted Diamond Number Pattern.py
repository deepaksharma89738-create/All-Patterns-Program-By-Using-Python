for i in range(1, 21):  
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(1, 2 * (21 - i)):
        print(k, end="")
    print()