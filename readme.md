# Book Shelf Management
## This is a Book shelf management program written in Python which uses Link List to save the Books.

### How are the books saved?
The books are saved in a linear data structured called Link list which holds data in individual objects named as nodes.

### Adding to the List
``` python
 def addtoshelf(self, bookname):
        NewNode = Node(bookname)
    
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=NewNode
```
In this code we can see how the books are saved and where are they save.Initially it checks if there is anything in the linklist or not by checking the first node of the List which is head if its Null/None it will save it else it will save next to the node which already have some data.
### Removing from the List
``` python
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
```
This code delete the node by searching it through the list.First it checks if the node is in in head and give it a none value to delete it.If its not in head then it traverses through the list and finds the node where its found a break statement is used and then its deleted by giving none value to it.
### Displaying The Books
``` python
 def displayshelfbooks(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

```
This code just traverses through the list and displays every value.

### Menu
* 1.Add a Book
 *   2.Remove A Book
  *  3.View All Books
   * 4.Exit/Quit

   User of the program gets this menu on there screen from which they can choose.Each Option menu leads to the function of the linklist and this is how books are added and removed from the shelf/List.