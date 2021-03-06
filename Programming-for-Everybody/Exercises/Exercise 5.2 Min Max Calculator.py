'''Min Max Calculator

    Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
    Once 'done' is entered, print out the largest and smallest of the numbers.
    If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
    Enter 7, 2, bob, 10, and 4 and match the output below.
'''
largest = -1
smallest = None

while True:
    string_input = input("Enter a number: ")
    if string_input == "done":
        break
    try:
        validinput = float(string_input)
    except:
        print("Invalid input")
        continue
    if validinput > largest:
        largest = validinput
    if smallest is None:
        smallest = validinput
    elif validinput < smallest:
        smallest = validinput
print("Maximum is", int(largest))
print("Minimum is", int(smallest))