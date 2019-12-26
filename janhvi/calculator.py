import re

print("Our Magical Calculator")
print("Type Quit to exit")

previous = 0
run = True


def perform_math():
    global run
    global previous 
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "Quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z.:()" ")]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)


while run:
    perform_math()
