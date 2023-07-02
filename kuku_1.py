for i in range(1, 10):
    for j in range(1, 10):
        if j < 9:
            print(f"{i*j}", end=" ")
        else:
            print(i * j)
