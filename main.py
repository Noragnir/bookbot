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

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        cara_count = count_characters(file_contents)
        print(word_count)
        print(cara_count)
main()


