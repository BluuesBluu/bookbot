
def count(content):
    words = content.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count(file_contents)
        print(f"{num_words} words found in the document")

if __name__ == '__main__':
    main()