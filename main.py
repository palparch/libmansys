import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

bookcsv = 'books.csv'

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
				'Issue_count': 0,
				'Date_issued': ''
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
	if not check_bid(bid, df):
		return
		
	bid = int(bid)
	print("Please enter the new data as prompted.")

	name = input("Enter the new name: ")
	author = input("Enter the new author's name: ")
	genre = input("Enter the new genre name: ")
	status = df.loc[bid-1, 'Status']
	issue_count = df.loc[bid-1, 'Issue_count']
	date_issued = df.loc[bid-1, 'Date_issued']

	df.loc[bid-1] = [bid, name, author, genre, status, issue_count, date_issued]
	df.to_csv(path_or_buf=bookcsv, sep=',', index=False)


# Delete a book
def delete_book():
	df = pd.read_csv(bookcsv)
	
	print()
	bid = input("Enter the book ID: ")
	
	if not check_bid(bid, df):
		return	

	bid = int(bid)
	print("Are you sure you want to delete book", bid, df.loc[bid-1, 'Name'], 'by', df.loc[bid-1, 'Author'], "?")
	response = input("Enter Yes or No to continue: ")

	if response == "no" or response == "No" or response == "NO":
		return

	
	newdf = df.drop(bid-1, axis=0)
		
	# change the bid and the index of all books
	newdf = newdf.reset_index(drop=True)
	newdf['Bid'] = range(1, len(newdf) + 1)
		
	newdf.to_csv(bookcsv, index=False)

	print("Successfully deleted the book", bid, df.loc[bid-1, 'Name'], 'by', df.loc[bid-1, 'Author'])



# Issue a book
def issue_book():
	df = pd.read_csv(bookcsv)
	bid = input("Enter the book ID: ")

	if not check_bid(bid, df):
		return	

	bid = int(bid)
	if df.loc[bid-1, 'Status'] == 'Issued':
		print("This book is already issued.")
		print("Therefore, it's not in the library.")
		print("Please try again with some other book.")
	
	else:
		df.loc[bid-1, 'Status'] = 'Issued'
		df.loc[bid-1, 'Issue_count'] += 1
		df.loc[bid-1, 'Date_issued'] = date.today()
		df.to_csv(path_or_buf=bookcsv, sep=',', index=False)
		print("Book succesfully issued.")



# Return
def return_book(bid):
	df = pd.read_csv(bookcsv)

	if not check_bid(bid, df):
		return	
		
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
def graph_books_by_genre():
	df = pd.read_csv(bookcsv)
	
	genre_freq = df.groupby('Genre')['Issue_count'].sum()

	plt.bar(genre_freq.keys(), genre_freq.values)
	plt.xlabel('Genres')
	plt.ylabel('Total no. of issues per genre')
	plt.xticks(rotation=45)
	plt.show()


def shorten_words(list1, length):
	wordlist = []
	letterlist = []
	for i in list1:
		wordlist.append(list(i))

	intermed_list = []
	j = 0

	for i in range(0, len(wordlist)):
		if len(wordlist[i]) < length:
			letterlist.append(wordlist[i])
		else:
			for j in range (0, length):
				intermed_list.append(str(wordlist[i][j]))
			intermed_list.append('...')
			letterlist.append(list(intermed_list))
			intermed_list = []
	
	finallist = []
	for i in letterlist:
		finallist.append("".join(i))
	
	return finallist



def graph_top_ten_books():
	df = pd.read_csv(bookcsv)
	df = df.sort_values(by='Issue_count', ascending=False)
	df = df.head(10)

	plt.barh(shorten_words(df.Name, 15)[::-1], df.Issue_count[::-1])
	plt.xlabel('Name of Books')
	plt.ylabel('Total no. of issues per books')
	plt.show()


def graph_top_authors():
	df = pd.read_csv(bookcsv)

	df = df.groupby('Author')['Issue_count'].sum()
	df = df.sort_values(ascending=False)
	df = df.head(10)

	plt.barh(shorten_words(df.keys(), 15)[::-1], df.values[::-1])
	plt.xlabel('No. of Issues')
	plt.ylabel('Authors')
	plt.show()


def generate_bill():
	df = pd.read_csv(bookcsv)
	libdf = pd.read_csv('libsetup.csv')
	bid = input('Enter the book ID: ')

	if not check_bid(bid, df):
		return	
		
	bid = int(bid)
	if df.loc[bid-1, 'Status'] == 'Available':
		print("This book is not currently issued.")
		return

	issue_date = pd.to_datetime(df.loc[bid-1, 'Date_issued']).date()
	today = date.today()
	days = max(0, (today - issue_date).days)
	per_day = float(libdf.loc[0, 'Per_day_charge'])
	fixed = float(libdf.loc[0, 'Fixed_charge'])
	max_days = int(libdf.loc[0, 'Maximum_days_allowed'])
	late_charge_per_day = float(libdf.loc[0, 'Late_charge_per_day'])
	late_days = max(0, days-max_days)

	if days > max_days:
		late_charge = late_days*late_charge_per_day
		day_charge = max_days*per_day
	else:
		late_charge = 0
		day_charge = days*per_day
	
	total = fixed + late_charge + day_charge

		## printing the bill in nice formatting
	print()
	print("=" * 55)
	print("                  CITY LIBRARY")
	print("              BOOK RETURN RECEIPT")
	print("=" * 55)

	print("Bill Date       :", date.today().strftime("%d-%m-%Y"))
	print("Book ID         :", bid)

	print("-" * 55)
	print("BOOK DETAILS")
	print("-" * 55)

	print("Book Name       :", df.loc[bid-1, 'Name'])
	print("Author          :", df.loc[bid-1, 'Author'])
	print("Date Issued     :", issue_date.strftime("%d-%m-%Y"))
	print("Date Returned   :", today.strftime("%d-%m-%Y"))
	print("Days Borrowed   :", days, "days")

	print("-" * 55)
	print("BILL BREAKDOWN")
	print("-" * 55)

	print("Fixed Charge    :", fixed, "/-")
	print("Daily Charge    :", day_charge, "/-", "(charged", per_day, "/- per day)")

	print("Late Charge     :", late_charge, "/-", "(charged", late_charge_per_day, "/- per day)")

	print("-" * 55)
	print("TOTAL BILL      :", total, "/-")
	print("=" * 55)

	print()
	print("Late Days       :", late_days, "days")
	print("Maximum Allowed :", max_days, "days")

	print("-" * 55)
	print("          Thank you for using our library!")
	print("             We hope you enjoyed your")
	print("                   reading! 📚")
	print("                Please visit again!")
	print("=" * 55)
	return_book(bid)


# Main menu
def menu():
	print("\n" + "=" * 50)
	print("	   📚 LIBRARY MANAGEMENT SYSTEM")
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
	print(" 12.  Generate Bill")
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
	bid = input("Enter the book ID: ")
	return_book(bid)

elif choice == '8':
	show_issued_books()

elif choice == '9':
	graph_books_by_genre()

elif choice == '10':
	graph_top_ten_books()

elif choice == '11':
	graph_top_authors()

elif choice == '12':
    generate_bill()

elif choice == '0':
	print("\nThank you for using the Library Management System!")

else:
	print("\nInvalid choice. Please enter a number from 0 to 12.")
