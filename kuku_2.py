line = int(input("行数を入力してください"))
columns = int(input("列数を入力してください"))

for i in range(1, line + 1):
    for j in range(1, columns):
        if j <= columns:
            print(f"{i*j}", end=" ")
    else:
        print(i * columns)
