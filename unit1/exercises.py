# Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
    print("Welcome to The Hundred Acre Wood!")  # I used a simple print statement to solve this problem

welcome() # Output: Welcome to The Hundred Acre Wood!


# Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}!")  # I used an f-string to include the name in the greeting

greeting("Laith")   # Welcome to The Hundred Acre Wood Laith!


'''
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character	Catchphrase
"Pooh"	"Oh bother!"
"Tigger"	"TTFN: Ta-ta for now!"
"Eeyore"	"Thanks for noticing me."
"Christopher Robin"	"Silly old bear."
If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"'
'''
def print_catchphrase(character):
    # I used a series of if-elif-else statements to match the character to their catchphrase
    if character == "Pooh":
        print("Oh brother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!") 

character = "Pooh"
print_catchphrase(character)    # Output: Oh brother!

character = "Piglet"
print_catchphrase(character)    # Output: Sorry! I don't know Piglet's catchphrase!


# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.
def get_item(items, x):
    if len(items) > x:
        if items[x] in items:
            return items[x]

    return None  # I used a simple if-else statement to check if x is a valid index and return the corresponding item or None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))  # Output: roo

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))  # Output: None



# Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().
def sum_honey(hunny_jars):
    sum_jars = 0
    for honey in hunny_jars:
        sum_jars += honey  # I used a for loop to iterate through the list and accumulate the sum of jars
    
    return sum_jars

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))   # Output: 14

hunny_jars = []
print(sum_honey(hunny_jars))   # Output: 0


# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
def doubled(hunny_jars):
    # Used list comprehension to double each value in the input list
    return [jar * 2 for jar in hunny_jars]

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))  # Output: [2, 4, 6]


# Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.
def reverse_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed list into a string
    return reversed_sentence

# Example usage:
sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))   # Output: fluff with stuffed all cubby little tubby