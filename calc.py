import math

s = input("データを入力してください(スペース区切り) >").split()
n = len(s)
sum = 0
max = 0
min = int(s[0])
for i in range(n):
    sum += int(s[i])

avg = math.floor(sum / n)

for j in range(n):
    if max < int(s[j]):
        max = int(s[j])

for j in range(n):
    if int(s[j]) < min:
        min = int(s[j])

print(f"合計値は{sum}")
print(f"最大値は{max}")
print(f"最小値は{min}")
print(f"平均値は{avg}")
