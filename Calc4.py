#Fourth iteration of the Calculator program, now with n-variable support for
#all functions.
#Unrelated to the program: https://www.reddit.com/r/learnprogramming/comments/6rtqjz/looking_for_fellow_beginners_learning_programming/

var=float(0)
ans=float(0)
total=float(0)
uI=float(0)
runApp=1
varNum=float(0)

addList=['1', 'Addition', 'addition', 'Add', 'add', 'A', 'a', '+']
subList=['2', 'Subtraction', 'subtraction', 'Subtract', 'subtract', 'S', 's', '-']
multList=['3', 'Multiplication', 'multiplication', 'Multiply', 'multiply', 'M', 'm', '*']
divList=['4', 'Division', 'division', 'Divide', 'divide', 'D', 'd', '/']
quitList=['5', 'Quit', 'quit', 'Q', 'q']

print('Calc 0.4. Coded by Jeren. Per Ardua, Ad Astra.')
while runApp==1:
    print("Please select operation: Addition, Subtraction, Multiplication, Division, Quit.")
    opSel=str(input(': '))
    if opSel in addList:
        varNum=float(input('Addition. Enter number of variables: '))
        while var<varNum:
            uI=float(input('Enter a number: '))
            total+=uI
            var+=float(1)
        if var==varNum:
            print(total)
            total=float(0)
            varAns=float(0)
            var=float(0)
            uI=float(0)
#This one was easiest; just tell the program to add 'uI' to 'total' with every
#iteration.
    elif opSel in subList:
        varNum=float(input('Subtraction. Enter number of variables: '))
        while var<varNum:
            uI=float(input('Enter a number: '))
            if var==float(0):
                total=uI
            else:
                total-=uI
            var+=float(1)
        if var==varNum:
            print(total)
            total=float(0)
            varAns=float(0)
            var=float(0)
            uI=float(0)
#The others were more difficult, but I had the aha moment when I realized that
#a simple else/if statement solved all problems.
    elif opSel in multList:
        varNum=float(input('Multiplication. Enter number of variables: '))
        while var<varNum:
            uI=float(input('Enter a number: '))
            if var==float(0):
                total=uI
            else:
                total*=uI
            var+=float(1)
        if var==varNum:
            print(total)
            total=float(0)
            varAns=float(0)
            var=float(0)
            uI=float(0)
    elif opSel in divList:
        varNum=float(input('Division. Enter number of variables: '))
        while var<varNum:
            uI=float(input('Enter a number: '))
            if var==float(0):
                total=uI
            else:
                total/=uI
            var+=float(1)
        if var==varNum:
            print(total)
            total=float(0)
            varAns=float(0)
            var=float(0)
            yu=float(0)
    elif opSel in quitList:
        print('Thank you for using Calc 0.3. See you space cowboy.')
        runApp=0
    else:
        print('Unknown command. Please try again.')
