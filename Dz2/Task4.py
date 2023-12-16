a = 0
sum = 0
max = 0
min = 0
first = True

while a != 7:
    a = int(input())

    sum += a
    print(sum)

    if a > max or first: max = a
    print(max)

    if a < min or first: min = a
    print(min)

    first = False

print("Goodbye!")