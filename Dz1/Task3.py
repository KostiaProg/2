start = int(input())
end = int(input())

for i in range(start, end):
    if i % 3 == 0: print("Fizz", end=" ")
    if i % 5 == 0: print("Buzz", end=" ")
    if i % 3 != 0 and i % 5 != 0: print(i, end=" ")
    print()