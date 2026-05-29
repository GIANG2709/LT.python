def kiem_tra_boi_so(n):
    if n % 13 == 0 or n % 19 == 0:
        return True
    return False


def kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or a == c or b == c:
            return "Tam giác cân"
        elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
    else:
        return "Không phải tam giác"


n = int(input("Nhập n: "))
if kiem_tra_boi_so(n):
    print(n, "là bội số của 13 hoặc 19")
else:
    print(n, "không là bội số của 13 hoặc 19")

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

print(kiem_tra_tam_giac(a, b, c))