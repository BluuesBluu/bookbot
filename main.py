
def count(content):
    words = content.split()
    print(len(words))


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count(file_contents)

if __name__ == '__main__':
    main()