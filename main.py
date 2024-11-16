def count_words(file_contents):
    return len(file_contents.split())

def count_character(file_contents):
    file_contents_lower = file_contents.lower()
    count_dict = {}
    for char in file_contents_lower:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_character(file_contents)
        print(f'--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n\n')
        for char, num in character_count.items():
            list_character_count = [{'character': char, 'num': num}]
            list_character_count.sort(reverse=True, key=sort_on)
            print(f"The '{char}' character was found {num} times")
        print('--- End report ---')

main()
