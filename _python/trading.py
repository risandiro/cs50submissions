balance = int(input("Account Balance: "))
while True:
    ticker, entry, stoploss = input("Ticker---Entry---Stoploss? ").split()

    ticker = ticker.upper()
    entry, stoploss = float(entry), float(stoploss)

    if entry > stoploss:
        risk = entry - stoploss
        target = entry + risk

    elif entry < stoploss:
        risk = stoploss - entry
        target = entry - risk

    risk_2 = int(((balance / 100) * 2) / risk)
    risk_15 = int(((balance / 100) * 1.5) / risk)
    risk_1 = int((balance / 100) / risk)

    print(f"{ticker} --> Target: {target}  Entry: {entry}  Stoploss: {stoploss}    Risk? 2%: -{risk_2}- 1.5%: -{risk_15}- 1%: -{risk_1}-")
