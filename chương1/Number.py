def number(x, y):
    for num in range(x, y + 1):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        
        if total < num:
            print(f"{num} là deficient.")
        elif total == num:
            print(f"{num} là perfect.")
        else:
            print(f"{num} là abundant.")

x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (y >= x): "))

print(f"Phân loại các số từ {x} đến {y}:")
number(x, y)