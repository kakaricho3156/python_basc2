# s = input("データを入力してください").split(" ")
# n = len(s)

# for i in range(n):
#     print(s[i])

s = input("データを入力してください(スペース区切り) >").split()
n = len(s)
sum = 0
max = 0
min = 0
for i in range(n):
    sum += int(s[i])

for j in range(n):
    if max < int(s[j]):
        max = int(s[j])

for j in range(n):
    k = j + 1
    if k > n-1:
        break
    elif int(s[j]) < int(s[k]):
        min = int(s[j])
    else:
        min = int(s[k])


print(f"合計値は{sum}")
print(f"平均値は{sum/n}")
print(f"最大値は{max}")
print(f"最小値は{min}")
