import random

list = []
for i in range(5):
    list.append(random.randint(1, 5))

for i in range(5):
    ans = int(input("<기회 {}번 남음> 1~5중에 아무 수나 골라보세요: ".format(5 - i)))
    if ans == list[i]:
        print("정답 !")
        break
    else:
        print("오답..")
        continue

print("결과 =", list)
print("Hi")