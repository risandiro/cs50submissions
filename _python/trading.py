balance = int(input("Account Balance: "))
ticker, entry, stoploss = input("Ticker---Entry---Stoploss? ").split()

ticker = ticker.upper()
entry, stoploss = float(entry), float(stoploss)

if entry > stoploss:
    target = entry - stoploss
elif entry < stoploss:
    target = stoploss - entry

risk_2 = ((balance / 100) * 2) * target
risk_15 = ((balance / 100) * 1.5) * target
risk_1 = (balance / 100) * target

print(f"{ticker} --> Target: {target + entry}  Entry: {entry}  Stoploss: {stoploss}    Risk? 2%: {risk_2} 1.5%: {risk_15} 1%: {risk_1}")
