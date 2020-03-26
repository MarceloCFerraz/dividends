def printResult(months, deposits, amount, dividends):
    print(
            "End of Year {0:^5} - Deposited $ {1:<17.2f} - Amount $ {2:<17.2f} - Dividends (year) $ {3:<17.2f} - Dividends (month) $ "
            "{4:<17.2f}".format(round(months / 12), deposits, amount, dividends * 12, dividends)
        )