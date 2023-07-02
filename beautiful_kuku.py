for i in range(1, 10):
    for j in range(1, 10):
        if i == 1 and j == 9:
            print(f"{i} * {j} =  {i*j} |")
        elif j < 9 and (i * j) < 10:
            print(f"{i} * {j} =  {i*j} |", end=" ")
        elif j < 9:
            print(f"{i} * {j} = {i*j} |", end=" ")
        else:
            print(f"{i} * {j} = {i*j} |")
