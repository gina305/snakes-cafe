menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Dessert": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}
# Set the status of the customer order
status = "Active"
""
# Loop through the dictionary and ask user for order until they'quit'

print("Menu: ", menu)

# Stretch Goals
# Print out a summary of complete order.
# Only allow ordering items on the menu.
# Allow ordering items not on menu but give custom reply.


# Dictionares to track the customer ordered items
items_ordered = {}
times_ordered = 0


def getOrder():
    while status == "Active":
        item = input(
            "************************************* What would you like to order? Type 'quit' to exit*************************************")

        if item == "quit":
            print('Your order: ',items_ordered)

            print('Thank you for your patronage!')
            break


            #Only order off the menu
        if item in menu["Appetizers"] or item in menu["Entrees"] or item in menu["Dessert"] or item in menu["Drinks"]:

         #Add to customer order
            if item in items_ordered:
                times_ordered = items_ordered[item] + 1
                # Change the number if previously ordered
                items_ordered[item] = times_ordered
                print(f"{items_ordered[item]} orders  of {item} have been added to your meal.")

            else:
                # Set default value to one
                items_ordered[item] = 1
                print(f"{items_ordered[item]} orders  of {item} have been added to your meal.")

        else:
            print(f"Sorry :-(, that's not on the menu. Hint: Case matters")

        # Increment item if user has already ordered it


# Run the function
getOrder()


