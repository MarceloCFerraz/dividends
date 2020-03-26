import questions, option1, option2

if __name__ == '__main__':
    divisor = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------ "
    finished = False
    option = 0

    print("------> WELCOME TO DIVIDEND CALCULATOR <------")
    print()
    print(divisor)

    while not finished:

        option = questions.mainMenu()

        print(divisor)

        if option == 1:
            option1.calculate()
        elif option == 2:
            option2.calculate()

        print(divisor)
        
        finished = questions.isFinished()
