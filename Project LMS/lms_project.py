# MINI PROJECT PYTHON LMS Library Management System

class LMS:
    """This class is used to keep records  of bookd library"""

    def __init__(self, listOfBooks, libraryName):
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        self.bookDict = {}
        id = 101
        with open(self.listOfBooks) as file:
            content = file.readlines()
        
        for line in content:
            self.bookDict.update({str(id):{'books_title':line.replace("\n",""),
            "lender_name":"", "status":"Available"}})
            id += 1
        
    def displayBooks(self):
        print("------------List Of Books-------------")
        print("BookID \t\t   Titile")
        print("----------------------------------------")
        for key, value in self.bookDict.items():
            print(key, "\t\t", value.get("books_title"),  " [",value.get("status"),"]")

    def issueBook(self):
        bookId = input("Enter a book ID : ")
        if bookId in self.bookDict.keys():
            if not self.bookDict[bookId]['status'] == "Available":
                print(f"This book is already Issued to {self.bookDict[bookId]['lender_name']} and BOOK ID is {bookId}")
            elif self.bookDict[bookId]['status'] == "Available":
                name = input("Enter your name")
                self.bookDict[bookId]['lender_name'] = name
                self.bookDict[bookId]['status'] = "Already Issued"
                print("Book Issued Successfully")
        else:
            print("Book Id Not Found")
    


try:
    lms = LMS("lms_file.txt", "Python LMS")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "Q": "Quit"}
    
    key_press = False

    while not (key_press == "q"):
        print(f"------Welcome to LMS -------------")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press Key : ").upper()
        if key_press == "I":
            print("\n Current Selection : ISSUE BOOK\n")
            lms.issueBook()
        elif key_press == "D":
            print("\n Current Selection : Display BOOK\n")
            lms.displayBooks()
        elif key_press == "Q":
            break
        else:
            continue   
except Exception as e:
    print(e)

