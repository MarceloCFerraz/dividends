import questions, result

def calculate():
    years = questions.getYears()
    amount = questions.getAmount()
    deposits = amount
    month_value = questions.getMonthValue()
    inflation = questions.getInflationMonth()
    growth_rate = questions.getGrowthRateMonth()
    reinvest_percentage = questions.getReinvestPercentage()

    months = 0

    real_rate = ((1 + (growth_rate * reinvest_percentage)) / (1 + inflation)) - 1

    while (months / 12) <= years:
        months += 1

        dividends = amount * real_rate

        deposits += month_value
        
        amount += dividends + month_value

        if months % 12 == 0:
            result.printResult(months, deposits, amount, dividends)
    # fora do while