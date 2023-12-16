start = int(input())
end = int(input())

even = 0
evenI = 0
odd = 0
oddI = 0
ninth = 0
ninthI = 0

for i in range(start, end):
    if i % 2 == 0:
        even += i
        evenI += 1
    else:
        odd += i
        oddI += 1
    if i % 9 == 0:
        ninth += i
        ninthI += 1

print(f"Even: {even}, {even/evenI}")
print(f"Odd: {odd}, {odd/oddI}")
print(f"Ninth: {ninth}, {ninth/ninthI}")