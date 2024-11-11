actual_cost = float(input("Please enter the actual product price (Pounds): "))
sale_amount = float(input("Please enter the sales amount(pounds: )"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {}".format(amount))
else:
    print("No profit. You are unsuccessful.Get better.Skill issue.")