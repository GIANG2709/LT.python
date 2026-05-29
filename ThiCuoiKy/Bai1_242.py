dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))
2.134
dien_tich_day = dai * rong
the_tich = dai * rong * cao

print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f} cm\u00b2")
print(f"Thể tích hình khối = {the_tich:.{so_le}f} cm\u00b3")