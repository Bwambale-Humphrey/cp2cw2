class Book:
    def __init__(self,title,author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def description_of_the_book(self) ->str:
        return f"{self.title} by {self.author} published in {self.year_published}."

#creating instances of two objects. 
book1 = Book("Lord of the rings", "JR Reuel", 1954)
book2 = Book("The treason of isengard","Christopher Tolkien", 1989)

#print the description
print(book1.description_of_the_book())
print(book2.description_of_the_book()) 

#sorting book list
def sort_books_by_year(books) ->list:
        # Check if the input is a list
        if not isinstance(book_list, list):
            raise ValueError("Input must be a list of Book objects.")
        
        #Empty list case
        if len(books) == 0:
            return []

        # Sort the list of books by year_published
        sorted_books = sorted(books, key=lambda book: book.year_published)
        return sorted_books

# Books list
book_list = [book1, book2]

# Sorting books
sorted_books = sort_books_by_year(book_list)
print("\nBooks sorted by year published:")
for book in sorted_books:
    print(book.description_of_the_book())

        #Showing the details of each book using loops
#for loop
print("\nBook details using For loop:")
for book in sorted_books:
    print(book.description_of_the_book())

#while loop
print("\nBook details using While loop:")
num = 0
while num < len(sorted_books):
    book = sorted_books[num]
    print(book.description_of_the_book())
    num +=1