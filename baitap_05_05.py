# Bài tập ngày 05/05
# Nội dung: Nhập list số nguyên dương và xử lý a, b, c, d

# ===== Nhập dữ liệu =====
L = []
while True:
    try:
        n = int(input("Nhập số nguyên dương (nhập số âm để dừng): "))
        if n < 0:
            break
        L.append(n)
    except:
        print("Vui lòng nhập số hợp lệ!")

print("\nList đã nhập:", L)

# ===== a) Tổng các số =====
print("\n--- Câu a ---")
tong = sum(L)
print("Tổng các số trong list:", tong)

# ===== b) Tổng khoảng cách giữa các cặp =====
print("\n--- Câu b ---")
tong_khoang_cach = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        tong_khoang_cach += abs(L[i] - L[j])

print("Tổng khoảng cách giữa các cặp số:", tong_khoang_cach)

# ===== c) Kiểm tra x =====
print("\n--- Câu c ---")
x = int(input("Nhập số x: "))
so_lan = L.count(x)

if so_lan > 0:
    print(f"{x} xuất hiện {so_lan} lần trong list")
else:
    print(f"{x} không có trong list")

# ===== d) So sánh x =====
print("\n--- Câu d ---")
if len(L) == 0:
    print("List rỗng!")
elif x > max(L):
    print("x lớn hơn tất cả các số trong list")
else:
    print("Các số lớn hơn x là:", end=" ")
    for num in L:
        if num > x:
            print(num, end=" ")