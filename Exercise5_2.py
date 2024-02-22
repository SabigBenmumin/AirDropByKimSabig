round = int(input("Enter number of products: "))
for i in range(round):
    price = float(input("Enter cost price: "))
    vat = price * 7 /100
    m_margin = price * 3 /100
    print(f"Cost price {price:,.2f} -> Selling price {price+vat+m_margin:,.2f}")