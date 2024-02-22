while True:
    amount = int(input("Enter the amount of sales: "))
    rate = float(input("Enter the commmision: "))
    commmision = amount * rate
    print(f"The commission is ${commmision:,.2f}")
    print("If your commission is greater than 3000, you can calculate again.")
    if commmision < 3000:
        break
    print("")