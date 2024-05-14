class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self, tu, dongnghia=None, trai_nghia=None):
        key = tu[0]  # Lấy ký tự đầu tiên của từ làm khóa trong từ điển
        if key in self.dictionary:
            self.dictionary[key].append((tu, dongnghia, trai_nghia))
        else:
            self.dictionary[key] = [(tu, dongnghia, trai_nghia)]

    def TraTu(self, tu):
        key = tu[0]  # Lấy ký tự đầu tiên của từ làm khóa trong từ điển
        if key in self.dictionary:
            for entry in self.dictionary[key]:
                if entry[0] == tu:
                    return entry[1], entry[2]  # Trả về từ đồng nghĩa và từ trái nghĩa
        return None, None  # Trả về None nếu từ không có trong từ điển

# Ví dụ
td = TuDien()
td.NhapTu("apple", "quả táo", "không có")
td.NhapTu("banana", "quả chuối", "không có")
td.NhapTu("car", "xe hơi", "không có")
td.NhapTu("dog", "con chó", "không có")

tu_dongnghia, tu_trainghia = td.TraTu("apple")
print("Từ đồng nghĩa của 'apple':", tu_dongnghia)
print("Từ trái nghĩa của 'apple':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("banana")
print("Từ đồng nghĩa của 'banana':", tu_dongnghia)
print("Từ trái nghĩa của 'banana':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("car")
print("Từ đồng nghĩa của 'car':", tu_dongnghia)
print("Từ trái nghĩa của 'car':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("dog")
print("Từ đồng nghĩa của 'dog':", tu_dongnghia)
print("Từ trái nghĩa của 'dog':", tu_trainghia)

tu_dongnghia, tu_trainghia = td.TraTu("cat")
print("Từ đồng nghĩa của 'cat':", tu_dongnghia)
print("Từ trái nghĩa của 'cat':", tu_trainghia)