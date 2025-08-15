# Exercise: Instantiate a custom Object
# This exercise demonstrates creating classes and objects in Python


# Step 1: Define a class called MyFirstClass
class MyFirstClass:
    # Step 1.2: Add a print statement inside the class
    print("Who wrote this?")

    # Step 2: Create a string variable named index and initialize it
    index = "Author-Book"

    # Step 3: Define a function called hand_list()
    def hand_list(self, philosopher, book):
        # Step 4.1: Print statement using the class variable
        print(MyFirstClass.index)

        # Step 4.2: Print statement with philosopher and book
        print(philosopher + " wrote the book: " + book)


# Step 5: Create and instantiate an object of that class
whodunnit = MyFirstClass()

# Step 5.2: Call method hand_list() over the object "whodunnit"
whodunnit.hand_list("Sun Tzu", "The Art of War")
