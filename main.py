from stats import*
import sys


def get_book_text(file_path):
  with open(file_path) as f:
    file_content=f.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    return text


text=main()




char_num=get_letter_num(text)
# char_num.sort(reverse=True,key=sort_on)
# print(char_num)

char_list = []

for char in char_num:
    char_dict = {}
    char_dict["char"] = char
    char_dict["num"] = char_num[char]
    char_list.append(char_dict)

sorted_list = sorted(char_list, key=sort_on, reverse=True)

print('============ BOOKBOT ============')
print("----------- Word Count ----------")
get_num_words(text)
print("--------- Character Count -------")

for item in sorted_list:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")

