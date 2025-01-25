
number_of_words = 0
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def word_count():
    words = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word = file_contents.split()
        words += len(word)
    return words

def character_count():
    characters = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for letter in file_contents:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
        return characters
    
def book_report():
    characters = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split_words = file_contents.split()
        for char in file_contents.lower():
            if char.isalpha():
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    dict_list = []
    for char, count in characters.items():
        dict_list.append({"char": char, "count": count})

    def sort_out(dict):
        return dict["count"]
    
    dict_list.sort(reverse=True, key=sort_out)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(split_words)} words found in the document\n")
    for item in dict_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

book_report()

if __name__ == '__main__':
    main()


print(f"total amount of words is: {word_count()}")
