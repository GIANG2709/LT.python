la_so_dong_nhat = lambda n: all(ch == str(n)[0] for ch in str(n))

la_so_hoan_thien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n

print("Các số đồng nhất từ 1 đến 10000:")
for i in range(1, 10001):
    if la_so_dong_nhat(i):
        print(i, end=" ")

print("\n\nCác số hoàn thiện từ 1 đến 10000:")
for i in range(1, 10001):
    if la_so_hoan_thien(i):
        print(i, end=" ")