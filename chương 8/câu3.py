class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.bai_hats = []

    def ThemBaiHat(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.bai_hats.append({"ten_bai_hat": ten_bai_hat, "ten_nhac_si": ten_nhac_si, "ten_ca_si": ten_ca_si})


class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        key = ten_album.lower()  # Hàm băm: chuyển tên album thành chữ thường
        if key not in self.dictionary:
            self.dictionary[key] = Album(ten_album)
        for bai_hat in danh_sach_bai_hat:
            self.dictionary[key].ThemBaiHat(bai_hat["ten_bai_hat"], bai_hat["ten_nhac_si"], bai_hat["ten_ca_si"])

    def XemAlbum(self, ten):
        key = ten.lower()
        if key in self.dictionary:
            album = self.dictionary[key]
            print("Tên album:", album.ten_album)
            print("Danh sách bài hát:")
            for bai_hat in album.bai_hats:
                print("- Tên bài hát:", bai_hat["ten_bai_hat"])
                print("  + Nhạc sĩ sáng tác:", bai_hat["ten_nhac_si"])
                print("  + Ca sĩ:", bai_hat["ten_ca_si"])
        else:
            print("Không tìm thấy album có tên", ten)


# Ví dụ minh họa
td = TuDien()
danh_sach_bai_hat_1 = [
    {"ten_bai_hat": "Gió mùa", "ten_nhac_si": "Nguyễn Văn Cường", "ten_ca_si": "Hương Tràm"},
    {"ten_bai_hat": "Em gái mưa", "ten_nhac_si": "Hoàng Tôn", "ten_ca_si": "Hương Tràm"},
]
danh_sach_bai_hat_2 = [
    {"ten_bai_hat": "Chạy ngay đi", "ten_nhac_si": "Sơn Tùng M-TP", "ten_ca_si": "Sơn Tùng M-TP"},
    {"ten_bai_hat": "Em của ngày hôm qua", "ten_nhac_si": "Sơn Tùng M-TP", "ten_ca_si": "Sơn Tùng M-TP"},
]
td.NhapAlbum("Hương Tràm", danh_sach_bai_hat_1)
td.NhapAlbum("Sơn Tùng M-TP", danh_sach_bai_hat_2)

print("Xem thông tin album Hương Tràm:")
td.XemAlbum("Hương Tràm")

print("\nXem thông tin album Sơn Tùng M-TP:")
td.XemAlbum("Sơn Tùng M-TP")

print("\nXem thông tin album không tồn tại:")
td.XemAlbum("Justin Bieber")