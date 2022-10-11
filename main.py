from random import randint

# -1-
c = []

for i in range(randint(0, 20)):
    c.append(randint(0, 20))

print(c)
print("max - ", max(c))
print("min - ", min(c))
# -2-
n = int(input("введите кол-во элементов"))
nums = []
for i in range(n):
    k = int(input("введите элемент"))
    nums.append(k)
print("list - ")
for i in range(n):
    nums[i] = nums[i] ** 2
print(nums)
# -3-
list = ["sdf", 2, "", '', 4, "edfef", 0]
list.remove("")
list.remove('')
print(list)
# -4-

n = int(input("введите кол-во элементов"))
num = []
for i in range(n):
    k = int(input("введите элемент"))
    num.append(k)
x = int(input("введите порог"))

for i in range(n - 1, -1, -1):
    if num[i] > x: num.pop(i)

print(num)
