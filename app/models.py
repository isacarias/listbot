# Initialize an empty list to store items
my_list = []


"""
Handles adding an item to the wishlist.

Args:
    text (str): The item to add to the wishlist.

Returns:
    str: Confirmation message.
"""
def add_item(text):
    global my_list  # Declare the list as global

    # Check if the text is empty or None
    if not text:
        return "Please provide an item to add."

    # Append the item to the list
    my_list.append(text)
    my_flist = '\n'.join(f"• {item}" for item in my_list)

    # Construct and return a confirmation message
    # NOTE: When Slack sends a command (request) its expecting an HTTP response
    # ie. Only the return statement sends data back to Slack
    return f"Added '{text}' to the list :acowq: \n\n:sparkles:Updated wishlist:sparkles:: \n{my_flist}"
    

"""
Handles removing an item from the wishlist.

Args: 
    text (str): The item to remove from the wishlist.

Returns:
    str: Confirmation message.
"""
def remove_item(text):
    global my_list  # Declare the list as global

    # Check if the text is empty or None
    if not text:
        return "Please provide an item to remove."

    # Check if the item is in the list
    if text in my_list:
        my_list.remove(text)  # Remove the item from the list
        my_flist = '\n'.join(f"• {item}" for item in my_list)
        return f"Removed '{text}' to the list :acowq: \n\n:sparkles:Updated wishlist:sparkles:: \n{my_flist}"
    
    else:
        return f"'{text}' is not in the list. Nothing to remove."