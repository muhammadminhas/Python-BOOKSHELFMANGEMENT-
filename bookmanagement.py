class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def addtoshelf(self, bookname):
        NewNode = Node(bookname)
    
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=NewNode
    def RemoveFromShelf(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def displayshelfbooks(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
choice=0
print("----------Book Shelf Management----------\n") 

ans=True
while ans:
    print("""
    1.Add a Book
    2.Remove A Book
    3.View All Books
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      bookname=input("Enter the book Name you want to put into the shelf:")
      list.addtoshelf(bookname)
    elif ans=="2":
      bookname=input("Enter the book Name you want to remove from the shelf:")
      list.RemoveFromShelf(bookname)
    elif ans=="3":
      list.displayshelfbooks()
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
