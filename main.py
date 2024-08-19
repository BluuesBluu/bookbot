
def count_word(content):
    words = content.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def count_characters(text):
    chars = {}
    chars_list = []
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    for c in chars:
        if c.isalpha() :
            chars_alpha = {"name": c, "num": chars[c]}
            chars_list.append(chars_alpha)
    #print(chars_list)
    return chars_list

def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = count_word(text)
    #num_char = count_characters(text)
    c_list =  count_characters(text)
    c_list.sort(reverse= True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for c in c_list:
        print(f"The '{c['name']}' character was found {c['num']} times")
    
    print("--- End report ---")
        

if __name__ == '__main__':
    main()