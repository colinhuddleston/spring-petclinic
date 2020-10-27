#x = 0 # Setup a variable to use for the conditional

#while x <= 10: # Continue looping until x is greater than 1
# print(x) # Print the current itterations value of x
#  x += 1 # Inrement x by 1 (add 1 to the current value of x)

#print("loop Finished") # This will execute after the loop since it's at a lower indentation level

#shopping_list = ["ham","eggs","cheese"]
#for items in shopping_list:
#    print (items)

#greeting = "Hello-World" # Setting up a string to iterate through

#for character in greeting: # Iterate over the string one letter at a time
#    if "-" in character: # if the current character is a hyphen
#        print("Hyphen detected, ending loop!")
#        break # End the loop
#    

#print("loop has exited")

#x = 0 # Initialize a variable to use in the condition

#while x < 10:
 #   x += 1
  #  if ((x % 2) == 0): # If the number is even
   #     print(x)

   # else: # If the number is odd
       # print(str(x)+"not an even number")
        #continue #go to next iteration

#shopping_lists = [["Eggs", "Milk", "Ham"], 
#                  ["Vinegar", "Mustard", "Ketchup"], 
#                  ["Burgers", "Lettuce", "Mayo"]]

#for current_list in shopping_lists: # Steps through the list of lists
#    for item in current_list: # Steps through each list
#        print(item) # Prints the item in the current shopping list


#while True: # This is an infinite loop
 # number = int(input("Please type a number between 1 and 10: ")) # Take user input

  #if number < 1: # Number is too small
  #  print("Number provided is less than 1")

  #elif number > 10: # Number is too large
  #  print("Number provided is greater than 10")

 # else: # If the input is in a valid range
   # print("number provided is between 1 and 10")
   # break # End the loop

#for number in range(5,11):
 #   print(number)

#for number in range(11):
#    print(number)

#def greet(name="John doe", greeting="Hello there: "):
#   """Greets a person with the greeting and their name

#   Parameters
#   ----------
#   name: (str)
# 
# def print_list(list_to_parse):
    # """TODO: Add docstring"""
    # """print_list(list_to_parse)
    #  Parameters
    #  ----------
    #  list_to_parse will be printed the full list

    #  Returns
    #  --------
    # printed list_to_parse:
    #     print(item)"""
    # result = print (list_to_parse) 

def delete_item(list_to_parse, item_index):
    
    """Takes a list, removes an item at the 
    specified index and returns the list
    Parameters
    ----------
    list_to_parse:
        The list to remove the item from
    item_index:
        The index to remove an item from
    Returns
    -------
    The list with the item removed
    """
    # Do stuff here
    pass # This just tells python to do nothing; remove it when you add your code
shopping_list = ["ham","egg","cheese"]
shopping_list = delete_item (shopping_list,[1])
print(shopping_list)
