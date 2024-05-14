class WordMeaning:
    def __init__(self, word_type, meaning, example):
        self.word_type = word_type
        self.meaning = meaning
        self.example = example

class Dictionary:
    def __init__(self):
        self.entries = {}  # Lưu từ điển dưới dạng bảng băm

    def add_word(self, word, word_type, meaning, example):
        if word in self.entries:
            self.entries[word].append(WordMeaning(word_type, meaning, example))
        else:
            self.entries[word] = [WordMeaning(word_type, meaning, example)]

    def remove_word(self, word):
        if word in self.entries:
            del self.entries[word]
            print(f"{word} đã được loại bỏ khỏi từ điển.")
        else:
            print(f"{word} không có trong từ điển.")

    def search_word(self, word):
        if word in self.entries:
            print(f"Thông tin về {word}:")
            for entry in self.entries[word]:
                print(f"- Loại từ: {entry.word_type}")
                print(f"  Nghĩa: {entry.meaning}")
                print(f"  Ví dụ: {entry.example}")
        else:
            print(f"{word} không có trong từ điển.")

    def save_to_file(self, filename):
        with open(filename, "w", encoding='utf-8') as file:  # Thêm encoding='utf-8'
            for word, meanings in self.entries.items():
                for meaning in meanings:
                    file.write(f"{word}\t{meaning.word_type}\t{meaning.meaning}\t{meaning.example}\n")


    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                word, word_type, meaning, example = line.strip().split("\t")
                self.add_word(word, word_type, meaning, example)


# Chương trình chính
def main():
    dictionary = Dictionary()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm từ mới vào từ điển")
        print("2. Loại bỏ một từ khỏi từ điển")
        print("3. Tra cứu từ trong từ điển")
        print("4. Lưu từ điển vào tập tin")
        print("5. Nạp từ điển từ tập tin")
        print("6. Kết thúc chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            word = input("Nhập từ mới: ")
            word_type = input("Nhập loại từ: ")
            meaning = input("Nhập nghĩa của từ: ")
            example = input("Nhập ví dụ: ")
            dictionary.add_word(word, word_type, meaning, example)
        elif choice == "2":
            word = input("Nhập từ cần loại bỏ: ")
            dictionary.remove_word(word)
        elif choice == "3":
            word = input("Nhập từ cần tra cứu: ")
            dictionary.search_word(word)
        elif choice == "4":
            filename = input("Nhập tên tập tin để lưu từ điển: ")
            dictionary.save_to_file(filename)
            print("Đã lưu từ điển vào tập tin", filename)
        elif choice == "5":
            filename = input("Nhập tên tập tin để nạp từ điển: ")
            dictionary.load_from_file(filename)
            print("Đã nạp từ điển từ tập tin", filename)
        elif choice == "6":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()