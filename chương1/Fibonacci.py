class Fibonacci:

    def recursive_fibonacci(n):
        if n <= 1:
            return n
        else:
            return Fibonacci.recursive_fibonacci(n - 1) + Fibonacci.recursive_fibonacci(n - 2)


    def iterative_fibonacci(n):
        if n <= 1:
            return n
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c

n = int(input("Nhập số nguyên n (n >= 0): "))
# Tính số Fibonacci bậc n bằng đệ qui
fib_recursive = Fibonacci.recursive_fibonacci(n)
# Tính số Fibonacci bậc n không đệ qui
fib_iterative = Fibonacci.iterative_fibonacci(n)

# In 
print(f"Số Fibonacci bậc {n} (đệ qui): {fib_recursive}")
print(f"Số Fibonacci bậc {n} (không đệ qui): {fib_iterative}")