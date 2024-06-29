from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Function to create the database and table
def create_table():
    conn = sqlite3.connect('books4.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_name TEXT,
            author TEXT,
            publisher TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Create the table when the application starts
create_table()

# Function to insert a new book
def insert_book(book_name, author, publisher):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (book_name, author, publisher)
        VALUES (?, ?, ?)
    ''', (book_name, author, publisher))
    conn.commit()
    conn.close()

# Function to retrieve all books
def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

# Function to retrieve a specific book by id
def get_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

# Function to update a book by id
def update_book(book_id, book_name, author, publisher):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE books
        SET book_name = ?, author = ?, publisher = ?
        WHERE id = ?
    ''', (book_name, author, publisher, book_id))
    conn.commit()
    conn.close()

# Function to delete a book by id
def delete_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

# API Endpoints

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book_name = data['book_name']
    author = data['author']
    publisher = data['publisher']
    insert_book(book_name, author, publisher)
    return jsonify({'message': 'Book created successfully'}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    books = get_books()
    return jsonify({'books': books})

# Get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_one_book(book_id):
    book = get_book(book_id)
    if book:
        return jsonify({'book': book})
    else:
        return jsonify({'message': 'Book not found'}), 404

# Update a book by id
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_one_book(book_id):
    data = request.json
    book_name = data.get('book_name')
    author = data.get('author')
    publisher = data.get('publisher')
    update_book(book_id, book_name, author, publisher)
    return jsonify({'message': 'Book updated successfully'})

# Delete a book by id
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_one_book(book_id):
    delete_book(book_id)
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
