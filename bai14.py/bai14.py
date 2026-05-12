# Chương trình đổi tiền thành số tờ ít nhất

# Danh sách mệnh giá tiền
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền
x = int(input("Nhap so tien X: "))

# Lưu số tiền ban đầu
so_tien_goc = x

# Biến đếm tổng số tờ
tong_to = 0

print(f"\nSo tien {so_tien_goc} duoc doi thanh:")

# Duyệt từng mệnh giá
for tien in menh_gia:

    # Tính số tờ
    so_to = x // tien

    # Cập nhật số tiền còn lại
    x = x % tien

    # In ra số tờ của từng loại
    print(f"Loai {tien} gom {so_to} to")

    # Cộng tổng số tờ
    tong_to += so_to

# In tổng số tờ
print(f"TONG CONG CO {tong_to} TO")