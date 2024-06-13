from library import Library
from book import Book


our_library = Library('Wseiz Library', 'Rejtana 17, Warsaw')

print("The name: ", our_library.name)

our_book = Book('A Song of Ice and Fire', 5280, 'epik fantezi', 'George R. R. Martin', '3423-kdsjflkdsjfkl')
our_library.add_book(our_book)