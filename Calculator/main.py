import re

print('Calculator Started!')
print('Type "quit" to exit\n')
previous = 0
run = True
print("Enter your equation:\n")


def perform_math():
    global run, previous
    equation = input('='+str(previous)+" ")
    if equation == 'quit':
        print('Goodbye')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            try:
                previous = eval(equation)
            except Exception as e:
                print(e)
        else:
            try:
                previous = eval(str(previous) + equation)
            except Exception as e:
                print(e)


while run:
    perform_math()