class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0].lower()  # Hàm băm: lấy ký tự đầu tiên của từ và chuyển thành chữ thường
        if key in self.dictionary:
            self.dictionary[key][tu] = {"dong_nghia": dong_nghia, "trai_nghia": trai_nghia}
        else:
            self.dictionary[key] = {tu: {"dong_nghia": dong_nghia, "trai_nghia": trai_nghia}}

    def DongNghia(self, tu):
        key = tu[0].lower()
        if key in self.dictionary and tu in self.dictionary[key]:
            return self.dictionary[key][tu]["dong_nghia"]
        return []

    def TraiNghia(self, tu):
        key = tu[0].lower()
        if key in self.dictionary and tu in self.dictionary[key]:
            return self.dictionary[key][tu]["trai_nghia"]
        return []
# Ví dụ minh họa
td = TuDien()
td.NhapTu("tốt", ["tốt đẹp", "xuất sắc"], ["xấu", "tệ"])
td.NhapTu("đẹp", ["xinh đẹp", "hấp dẫn"], ["xấu", "khó xử"])
td.NhapTu("xấu", ["xấu xí", "khó chịu"], ["tốt", "đẹp"])

tu_can_tra = "tốt"
print("Từ đồng nghĩa của", tu_can_tra + ":", td.DongNghia(tu_can_tra))
print("Từ trái nghĩa của", tu_can_tra + ":", td.TraiNghia(tu_can_tra))

tu_can_tra = "đẹp"
print("Từ đồng nghĩa của", tu_can_tra + ":", td.DongNghia(tu_can_tra))
print("Từ trái nghĩa của", tu_can_tra + ":", td.TraiNghia(tu_can_tra))

tu_can_tra = "xấu"
print("Từ đồng nghĩa của", tu_can_tra + ":", td.DongNghia(tu_can_tra))
print("Từ trái nghĩa của", tu_can_tra + ":", td.TraiNghia(tu_can_tra))