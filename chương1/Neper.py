class Neper:
    def naper_sum(n):
        result = 0
        factorial = 1
        for k in range(n + 1):
            result += 1 / factorial
            factorial *= (k + 1)
        return result

n = int(input("Nhập số nguyên n (n >= 0): "))

# Tính tổng của các số hạng từ a0 đến an
naper_result = Neper.naper_sum(n)
print(f"Tổng của a0 + a1 + ... + a{n} là: {naper_result}")