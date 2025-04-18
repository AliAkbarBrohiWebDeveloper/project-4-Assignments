# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# # Print the length of the list.


# # Add 'mango' at the end of the list. 


# # Print the updated list.
# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.

# def main():
#     # Create a list of fruits
#     fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

#     # Print the length of the list
#     print("Length of the fruit list:", len(fruit_list))

#     # Add 'mango' at the end of the list
#     fruit_list.append('mango')

#     # Print the updated list
#     print("Updated fruit list:", fruit_list)



  

# # Run the main function
# if __name__ == "__main__":
#     main()






def access_element(lst, index):
    # Function to access the element at a specified index
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    # Function to modify the element at the specified index
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} modified to {new_value}."
    else:
        return "Index out of range."

def slice_list(lst, start_index, end_index):
    # Function to slice the list
    if start_index < 0 or end_index > len(lst) or start_index >= end_index:
        return "Invalid range."
    else:
        return lst[start_index:end_index]

def game():
    # A sample list to interact with
    sample_list = [12, 'apple', 4.5, 'banana', 100]

    # Game instructions
    print("Welcome to the Index Game!")
    print("You can perform 3 operations on the list:")
    print("1. Access an element by index")
    print("2. Modify an element by index")
    print("3. Slice the list")

    while True:
        # Ask for operation choice
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter the operation number: ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            print("Element:", access_element(sample_list, index))

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(sample_list, index, new_value))

        elif choice == '3':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            print("Sliced list:", slice_list(sample_list, start_index, end_index))

        elif choice == '4':
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    game()
