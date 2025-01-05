def count_words(file_contents):
        word = file_contents.split()
        count = len(word)
        return(count)

def count_characters(file_contents):
        lowered_file = file_contents.lower()
        char_count ={}
        for char in lowered_file:
                if char in char_count:
                        char_count[char] += 1
                else:
                        char_count[char] = 1
        return char_count

def sort_on(dict):
        return dict["num"]


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_characters(file_contents)
        chara_lists = []
        for char, count in char_counts.items():
                if char.isalpha():
                        chara_lists.append({"chara": char, "num": count})
        chara_lists.sort(reverse=True, key=sort_on)
        print("--- Begin reports of books/books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for chara_dict in chara_lists:
                print(f"The '{chara_dict['chara']}' character was found {chara_dict['num']} times")
        print("--- End report ---")
main()


