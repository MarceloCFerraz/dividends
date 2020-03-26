import questions, result

def calculate():
    amount = questions.getAmount()
    deposits = amount
    goal = questions.getGoal(amount)
    month_value = questions.getMonthValue()
    inflation = questions.getInflationMonth()
    growth_rate = questions.getGrowthRateMonth()
    reinvest_percentage = questions.getReinvestPercentage()

    months = 0
    
    real_rate = ((1 + (growth_rate * reinvest_percentage)) / (1 + inflation)) - 1

    while amount < goal:
        months += 1

        dividends = amount * real_rate

        deposits += month_value

        amount += dividends + month_value

        if months % 12 == 0 or amount >= goal:
            result.printResult(months, deposits, amount, dividends)

    # fora do while

    # return ("# YOU WILL ACHIEVE YOUR GOAL OF ${0} IN ABOUT {1} YEARS ({2} MONTHS).\nTHE LAST DIVIDEND RECEIVED WAS "
    #        "APPROXIMATELY ${3} #".format(goal, round(months / 12), months, round(dividends)))