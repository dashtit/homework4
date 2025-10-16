import yaml


def add_book(title, author, year, filename):
    book = {
        'author': author,
        'title': title,
        'year': year
    }
    save_books(book, filename)


def save_books(book, filename):
    books = read_books(filename)
    books.append(book)
    with open(filename, 'w', encoding='utf-8') as file:
        yaml.dump({'books': books}, file, allow_unicode=True)


def read_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        books = yaml.safe_load(file)
        return books.get('books')
