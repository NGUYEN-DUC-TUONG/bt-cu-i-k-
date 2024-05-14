def pascal(n):
    for i in range(n):
        coef = 1  # Hệ số cho mỗi số hạng trong hàng
        for j in range(1, n - i + 1):
            print(" ", end="")
        
        for j in range(0, i + 1):
            #  In ra hệ số hiện tại
            print(" ", coef, sep="", end="")
            coef = coef * (i - j) // (j + 1)
        print()

n = int(input("Nhập số nguyên dương n: "))

pascal(n)