balance = int(input("Account Balance: "))
while True:
    ticker, entry, stoploss = input("Ticker---Entry---Stoploss? ").split()

    ticker = ticker.upper()
    entry, stoploss = float(entry), float(stoploss)

    if entry > stoploss:
        target = entry + stoploss
    elif entry < stoploss:
        target = entry - (stoploss - entry)

    risk_2 = int(((balance / 100) * 2) * target)
    risk_15 = int(((balance / 100) * 1.5) * target)
    risk_1 = int((balance / 100) * target)

    print(f"{ticker} --> Target: {target}  Entry: {entry}  Stoploss: {stoploss}    Risk? 2%: -{risk_2}- 1.5%: -{risk_15}- 1%: -{risk_1}-")
