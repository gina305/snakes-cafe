print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
)

# initialize empty meal dictionary

# start loop here until user enters quit

# create a variable to store the user's order
order = input("> ")
init_dict = {}
init_dict["Newzealand"] = [67,29,87]
init_dict["Switzerland"] = [118,490,289]
init_dict["Polland"] = [102,201,801]

print("Created dictionary with list items:",init_dict)
# loop to ask user for item until order is complete

#  items[order]=items[order] + 1

    # print the order in some fancy way we're still figuring out
    num_items = 1
# TODO: properly tally items that have been ordered
    report = f"** {num_items} order of {order} have been added to your meal **"

    print(report)
# end loop 23