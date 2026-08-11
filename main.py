import pandas as pd

bookcsv = 'books.csv'


# Initialise csv file if it doesn't exist


# Add a book
def add_book():
	df = pd.read_csv(bookcsv)
	
	name = input('Enter the name of the book: ')
	author = input('Enter the name of the author: ')
	genre = input('Enter the genre: ')
	
	bookdict = {
				'Bid': int(len(df)+1),
				'Name': name,
				'Author': author,
				'Genre': genre
			}

	df.loc[len(df)] = bookdict
	df.to_csv(path_or_buf=bookcsv, sep=',', index=False)



# Display books
def display_books():
	df = pd.read_csv(bookcsv)
	print(df)


# Search a book
def search_book_by_bid():
	df = pd.read_csv(bookcsv)
	bid = int(input("Enter the book ID: "))
	print(df.loc[int(bid-1)])

	
def search_book_by_name(book_name):
	df = pd.read_csv(bookcsv)
	print(df)
	print(df.loc[book_name])


#book_name = input()
#search_book_by_name(book_name)
# Update a book


# Delete


# Issue


# Return


# Show avaiable


# Show issued


# Count books


# Books by genre


# Most borrowed books


# Top authors


# Exit program







# Main menu
def menu():
    print("\n" + "=" * 50)
    print("           📚 LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("  1.  Add a New Book")
    print("  2.  Update Book")
    print("  3.  Delete Book")
    print("  4.  Search Book")
    print("  5.  Display All Books")
    print("  6.  Issue Book")
    print("  7.  Return Book")
    print("  8.  Show Issued Books")
    print("  9.  Generate Genre-wise Graph")
    print(" 10.  Generate Most Borrowed Books Graph")
    print(" 11.  Generate Top Authors Graph")

    print("\n  0.  Exit")
    print("=" * 50)


while True:
    menu()

    choice = input("\nEnter your choice: ")

    if choice == '1':
        add_book()

    elif choice == '2':
        update_book()

    elif choice == '3':
        delete_book()

    elif choice == '4':
        print("\nSearch Book")
        print("-" * 30)
        print("1. Search by Book ID")
        print("2. Search by Book Name")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            search_book_by_bid()

        elif choice == '2':
            search_book_by_name()

        else:
            print("\nInvalid choice.")


    elif choice == '5':
        display_all_books()

    elif choice == '6':
        issue_book()

    elif choice == '7':
        return_book()

    elif choice == '8':
        show_issued()

    elif choice == '9':
        books_by_genre()

    elif choice == '10':
        most_borrowed()

    elif choice == '11':
        top_authors()

    elif choice == '0':
        print("\nThank you for using the Library Management System!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 0 to 11.")
