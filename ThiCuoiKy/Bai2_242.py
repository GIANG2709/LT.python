def in_bang_cuu_chuong(a, b):
    if a < b:
        ds = range(a, b + 1)
    else:
        ds = range(a, b - 1, -1)

    for i in ds:
        print(f"\nBảng cửu chương {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def liet_ke_nguyen_to_nho_hon_n(n):
    for i in range(2, n):
        if la_nguyen_to(i):
            print(i, end=" ")
    print()


def uoc_so_la_nguyen_to(n):
    for i in range(1, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            print(i, end=" ")
    print()


a, b = map(int, input("Nhập 2 số nguyên a, b: ").split(","))
in_bang_cuu_chuong(a, b)

n = int(input("\nNhập số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn n:")
liet_ke_nguyen_to_nho_hon_n(n)

print("Các ước số của n là số nguyên tố:")
uoc_so_la_nguyen_to(n)