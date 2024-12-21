import time

start = time.time()
total = 0
for i in range(10**7):
    total += i * (i + 1) // 2  # Multiplication, addition, division
end = time.time()

print("Integer Arithmetic Time:", end - start)