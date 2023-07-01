#Project1

class book():
    def __init__(self, ibsn, title, cat, pub, year_pub):
        self.__pk = ibsn
        self.__title = title
        self.__cat = cat
        self.__pub = pub
        self.__yearPub = year_pub

    def set_pk(self, ibsn):
        self.__pk = ibsn

    def get_pk(self):
        return self.__pk

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_cat(self, cat):
        self.__cat = cat

    def get_cat(self):
        return self.__cat

    def set_pub(self, pub):
        self.__pub = pub

    def get_pub(self):
        return self.__pub

    def set_yearPub(self, year_pub):
        self.__yearPub = year_pub

    def get_yearPub(self):
        return self.__yearPub


def menu():
    print('########################################################\n' +
          'Please enter an option for accessing the Books! database\n' +
          "1. Display all books' records stored\n" +
          '2. Add a new book into Books! database records\n' +
          '3. Sort books by Category and list books\n' +  # Ascending using Bubble Sort
          '4. Sort books by Publisher and list books\n' +  # Descending using Selection Sort
          '0. Exit the Books! database\n' +
          '#######################################################')


def display_book():
    count = 0
    for i in book_list:
        count +=1
        print('\nBook #%d' %count)
        print('----------------------')
        print('Book IBSN: %s' %i.get_pk())
        print('Book Title: %s' %i.get_title())
        print('Book Category: %s' %i.get_cat())
        print('Book Publisher: %s' %i.get_pub())
        print('Year Published: %s\n' %i.get_yearPub())


def set_book():
    check = True
    while check:
        pk = input("Please enter the IBSN of the book: ")
        while True:
            if pk != '':
                if pk.isnumeric():
                    if int(pk) <= 0:
                        print('Please enter a valid IBSN for the book!')
                        pk = input("Please enter the IBSN of the book: ")
                    else:
                        break
                else:
                    print('IBSN cannot have alphanumeric characters or spaces!')
                    pk = input("Please enter the IBSN of the book: ")
            else:
                print('Please input an IBSN!')
                pk = input("Please enter the IBSN of the book: ")

        for i in book_list:
            tmp = i.get_pk()
            if int(pk) == tmp:
                print('Book IBSN already exists, please enter another IBSN!')
                pk = input("Please enter the IBSN of the book: ")
            else:
                pass


        title = input("Please enter the name of the book: ")
        while True:
            if title.replace(" ", "") != '':
                break
            else:
                print('Name of book cannot be empty!')
                title = input("Please enter the name of the book: ")

        cat = input("Please enter Category of the book: ")
        while True:
            if cat.replace(" ", "") != '':
                break
            else:
                print('Category of the book cannot be empty!')
                cat = input("Please enter Category of the book: ")

        pub = input("Please enter the Publisher of the book: ")
        while True:
            if pub.replace(" ", "") != '':
                break
            else:
                print("Name of publisher cannot be blank!")
                pub = input("Please enter the Publisher of the book: ")

        pub_year = int(input("Please enter the Year it was Published: "))
        while True:
            if (pub_year <= 1499) or (pub_year >= 2024):
                print('Please enter a valid Year between 1500 and 2023 inclusive!')
                pub_year = int(input("Please enter the Year it was Published: "))
            else:
                break

        tmp = book(int(pk), title, cat, pub, pub_year)
        book_list.append(tmp)


        print('\nBook IBSN %s has been added!\n' %pk)
        check = False


def sort_cat():
    n = len(book_list)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if book_list[j].get_cat().upper() > book_list[j + 1].get_cat().upper():
                # Swap the j and j+1 items
                tmp = book_list[j]
                book_list[j] = book_list[j + 1]
                book_list[j + 1] = tmp

    display_book()


def sort_pub():
    n = len(book_list)
    for i in range(n - 1):
        #Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if book_list[j].get_pub().upper() > book_list[smallNdx].get_pub().upper():
                smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest
                # value is not already in its proper position.
        if smallNdx != i:
            tmp = book_list[i]
            book_list[i] = book_list[smallNdx]
            book_list[smallNdx] = tmp

    display_book()


v = book(11, 'Days in The Wild West', 'Adventure', 'Oliver John', 1999)
x = book(21, 'Gimai Seikatsu', 'Romance', 'Mikawa Ghost', 2018)
y = book(69, 'Asterisk War', 'Action', 'Miyazaki Yuu', 2016)
z = book(23, 'Angel Next Door Spoils me Rotten', 'Romance', 'Saekisan', 2019)
j = book(17, 'Isekai wa Smartphone to Tomo ni', 'Adventure', 'Fuyuhara Patora', 2015)
book_list = [v, x, y, z, j]



while True:
    try:
        menu()
        choice = int(input("\nChoice: "))
        if choice == 1:
            display_book()
        elif choice == 2:
            set_book()
        elif choice == 3:
            sort_cat()
        elif choice == 4:
            sort_pub()
        elif choice == 0:
            print('\n###############################\n'+
                  '#Thank you, see you next time!#\n'+
                  '###############################\n')
            break
        else:
            print('\nPlease enter a valid option!\n')

    except ValueError:
        print('\nPlease enter a valid integer, returning to home screen!\n')

    except:
        print("\nUnexpected error please try again\n")
