start = int(input())
end = int(input())

fifth = 0

for i in range(start, end):
    print(i)
    if i % 5 == 0: fifth += 1
print()

for i in range(end, start, -1):
    print(i)
print()
    
for i in range(start, end):
    if i % 7 == 0: print(i)
print()

print(fifth)