import pandas as pd
import matplotlib.pyplot as plt

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
				'Genre': genre,
				'Status': 'Available',
				'Issue_count': 0
			}

	df.loc[len(df)] = bookdict
	df.to_csv(path_or_buf=bookcsv, sep=',', index=False)


def check_bid(bid, df):
	# check if bid is an integer
	try:
		bid = int(bid)
	except:
		print("Book ID can only be an integer value. Please try again.")
		return False

	if type(bid) != int:
		print("Book ID can only be an integer value. Please try again.")
		return False

	# check if bid exists in our csv records
	bidlist = list(df['Bid'])

	if bid in bidlist:
		return True
	else:
		print("This book ID doesn't exist. Please try again with an existing book ID.")
		return False




# Display books
def display_books():
	df = pd.read_csv(bookcsv)
	print(df)


# Search a book
def search_book_by_bid():
	df = pd.read_csv(bookcsv)
	bid = input("Enter the book ID: ")
	if check_bid(bid, df):
		print(df.loc[int(bid)-1])


	
def search_book_by_name():
	df = pd.read_csv(bookcsv)
	book_name = input("Enter the name of the book: ")

	# check if book name exists in df
	namelist = list(df['Name'])

	if book_name not in namelist:
		print("This book '" + book_name + "' doesn't exist in the records.")
		return

	result = df[df["Name"] == book_name]
	print(result)


# Update a book
def update_book():
	df = pd.read_csv(bookcsv)
	bid = input("Enter the book ID: ")
	if check_bid(bid, df):
		bid = int(bid)
		print("Please enter the new data as prompted.")

		name = input("Enter the new name: ")
		author = input("Enter the new author's name: ")
		genre = input("Enter the new genre name: ")
		status = df.loc[bid-1, 'Status']
		issue_count = df.loc[bid-1, 'Issue_count']

		df.loc[bid-1] = [bid, name, author, genre, status, issue_count]
		df.to_csv(path_or_buf=bookcsv, sep=',', index=False)


# Delete a book
def delete_book():
	df = pd.read_csv(bookcsv)
	
	print()
	bid = input("Enter the book ID: ")
	
	if check_bid(bid, df):
		bid = int(bid)
		print("Are you sure you want to delete book", bid, df.loc[bid-1, 'Name'], 'by', df.loc[bid-1, 'Author'], "?")
		response = input("Enter Yes or No to continue: ")

		if response == "no" or response == "No":
			return

	
		newdf = df.drop(bid-1, axis=0)
		newdf.to_csv(bookcsv, index=False)
		print("Successfully deleted the book", bid, df.loc[bid-1, 'Name'], 'by', df.loc[bid-1, 'Author'])



# Issue a book
def issue_book():
	df = pd.read_csv(bookcsv)
	bid = input("Enter the book ID: ")

	if check_bid(bid, df):
		bid = int(bid)
		if df.loc[bid-1, 'Status'] == 'Issued':
			print("This book is already issued.")
			print("Therefore, it's not in the library.")
			print("Please try again with some other book.")
	
		else:
			df.loc[bid-1, 'Status'] = 'Issued'
			df.loc[bid-1, 'Issue_count'] += 1
			df.to_csv(path_or_buf=bookcsv, sep=',', index=False)
			print("Book succesfully issued.")



# Return
def return_book():
	df = pd.read_csv(bookcsv)
	bid = input("Enter the book ID: ")

	if check_bid(bid, df):
		bid = int(bid)

		if df.loc[bid-1, 'Status'] == 'Available':
			print("This book is already avalaible in the library.")
			print("Please try again with some other book.")	
			return
		
		df.loc[bid-1, 'Status'] = 'Available'
		df.to_csv(path_or_buf=bookcsv, sep=',', index=False)
		print("Book succesfully returned.")




# Show issued
def show_issued_books():
	df = pd.read_csv(bookcsv)

	print("\nIssued Books")
	print("-" * 30)

	print('This is the list of issued books:')
	print(df[df.loc[:, 'Status'] == 'Issued'])


## GRAPHS

# Books by genre
# here, we'll print a graph for books by genre to see which book is popular in which genre
#def unique_values(list1):
#	for i in list1:
#		print(i)
#		newlist = list1.remove(i)
#		print(newlist)
#		for j in list(newlist):
#			issue_count = 0
#			if i == j:


def graph_books_by_genre():
	df = pd.read_csv(bookcsv)
	
	genres = list(df.Genre)
	issue_count = list(df.Issue_count)
	
	

	print(issue_freq)

	#plt.plot(df.Genre, )
	#plt.show()


# Most borrowed books
# here, we will just show a graph for number of issues per book




# Top authors
# here idk which type of graph ill use here
# but yeah the purpose will be to compare authors on the basis of number of issues all time





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
    display_books()

elif choice == '6':
    issue_book()

elif choice == '7':
    return_book()

elif choice == '8':
	show_issued_books()

elif choice == '9':
    graph_books_by_genre()

elif choice == '10':
    graph_most_borrowed()

elif choice == '11':
    graph_top_authors()

elif choice == '0':
    print("\nThank you for using the Library Management System!")

else:
    print("\nInvalid choice. Please enter a number from 0 to 11.")
