
x = 1
for i in range(1000):
    x = x*2

total = 0
for num in str(x):
    total += int(num)
print (total)