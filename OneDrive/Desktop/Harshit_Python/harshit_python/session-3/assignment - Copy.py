# Question 1/10
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num == 3:
        break
    total += num
print(total)

# Question 2/10
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
print(num)

# Question 3/10
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)

# Question 4/10
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

# Question 5/10
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')

# Question 6/10
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    if num % 2 != 0: 
        total += num
print(total)

# Question 7/10
x = 5
y = 3
if x > y:
    if x % y == 0:
        print("x is divisible by y")
    else:
        print("x is not divisible by y")
else:
    print("Invalid comparison")

# Question 8/10
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        break
    print(num)
else:
    print("All numbers are even")

# Question 9/10
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')
else:
    if i == 5:
        print("Loop completed successfully", end=' ')

# Question 10/10
x = 100
while x > 0:
    print(x, end=' ')
    x = x // 2
