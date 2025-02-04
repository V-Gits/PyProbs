#Find the large digit in a two-digit number
NUM = int(input("Enter the two digit Number: "))
if NUM >= 10 and NUM <= 99:
    UnitDigit = NUM%10
    TensDigit = NUM//10
    if UnitDigit == TensDigit:
        print(f"The Unit Digit {UnitDigit} and Tens Digit {TensDigit} are same")
    elif UnitDigit > TensDigit:
        print(f"The Unit Digit {UnitDigit} is greater than Tens Digit {TensDigit}")
    else:
        print(f"The Tens Digit {TensDigit} is greater than Unit Digit {UnitDigit}")