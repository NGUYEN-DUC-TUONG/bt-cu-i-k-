class GCD:
    def gcd_recursive(m, n):
        if n == 0:
            return m
        else:
            return GCD.gcd_recursive(n, m % n)
        
    def gcd_iterative(m, n):
        while n != 0:
            m, n = n, m % n
        return m

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
# Tính và in ra ước số chung lớn nhất của m và n đệ qui
gcd_recursive_result = GCD.gcd_recursive(m, n)
print(f"Ước số chung lớn nhất của {m} và {n} là (dùng đệ qui): {gcd_recursive_result}")
# Tính và in ra ước số chung lớn nhất của m và n không đệ qui
gcd_iterative_result = GCD.gcd_iterative(m, n)
print(f"Ước số chung lớn nhất của {m} và {n} là (không dùng đệ qui): {gcd_iterative_result}")
