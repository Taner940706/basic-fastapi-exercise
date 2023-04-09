from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': "Title One", 'author': 'Ivan', 'category': 'science'},
    {'title': "Title Two", 'author': 'Author Two', 'category': 'Category Two'},
    {'title': "Title Three", 'author': 'Author Three', 'category': 'Category Three'},
    {'title': "Title Four", 'author': 'Author Four', 'category': 'Category Four'},
    {'title': "Title Five", 'author': 'Author Five', 'category': 'Category Five'},
    {'title': "Title Six", 'author': 'Author Six', 'category': 'Category Six'},
]


@app.get('/')
def get_all_books():
    return BOOKS


@app.get('/books/{book_title}')
def get_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('books/{book_author}')
def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and \
                book.get('author').casefold() == book_author.casefold():
            book_to_return.append(book)
    return book_to_return


@app.post('books/create_book/')
async def add_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('books/update-book/')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('books/delete-book/{book_title}')
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title') == book_title.casefold():
            BOOKS.pop(i)
            break