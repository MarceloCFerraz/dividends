import math

divisor = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------ "

def mainMenu():
    valid = False

    while not valid:
            print("- PLEASE SELECT A VALID OPTION -")
            print("[1] Discover how much your money will yield in a determined period of time")
            print("[2] Discover how long will it take for you to conquer your goal")
            option = int(input(" -> "))
            valid = (option == 1 or option == 2)

    return option

def isFinished():
    
    verify = input("If you want to EXIT THIS PROGRAM, type '0', if you don't, type anything and hit ENTER\n-> ")
    finished = (verify == "0")

    return finished

def getYears(): 
    valid = False
    
    while not valid:
        years = float(input("Type how many YEARS you want your investment to yield\n -> "))
        print(divisor)

        valid = (years > 0)

    return years

def getAmount():    
    valid = False

    while not valid:    
        amount = float(input("Type the INITIAL AMOUNT (amount > 0)\n -> "))
        print(divisor)

        valid = (amount > 0)

    return amount

def getGoal(amount):    
    valid = False

    while not valid:
        goal = float(input("Type your GOAL (goal > amount) \n -> "))
        print(divisor)

        valid = (goal > amount)

    return goal

def getMonthValue(): 
    valid = False

    while not valid:
        month_value = float(input("Type the AMOUNT PER MONTH (value > 0)\n -> "))
        print(divisor)

        valid = (month_value >= 0)

    return month_value

def getInflation():
    inflation = float(input("Type the MEDIUM INFLATION RATE PER YEAR\n -> "))
    inflation /= 100
    print(divisor)

    return inflation

def getInflationMonth():
    inflation = math.pow(1 + getInflation(), 1/12) - 1
    
    return inflation

def getGrowthRate():
    valid = False

    while not valid:
        percentage = float(input("Type the MEDIUM GROWTH RATE PER YEAR (percentage > 0)\n -> "))
        percentage = percentage / 100
        # percentage = math.pow(percentage, 1/12) # Taxa efetiva de ano para mês
        print(divisor)

        valid = (percentage > 0)

    return percentage

def getGrowthRateMonth(): 
    percentage = math.pow(1 + getGrowthRate(), (1/12)) - 1

    return percentage

def getReinvestPercentage(): 
    valid = False

    while not valid:
        percentage = float(input("Type the REINVEST PERCENTAGE (0 < percentage <= 100)\n -> "))
        percentage = percentage / 100
        print(divisor)

        valid = (0 < percentage <= 1)

    return percentage
