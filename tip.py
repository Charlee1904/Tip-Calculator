print("Tip Calculator")
bill_total = input("What was the bill total?")
tip_amount = input("How much would you like to tip? 10, 15, or 20?")
split = input("how many are in your party?")
total = bill_total + split

bill_total_int = int(bill_total)
tip_amount_int = int(tip_amount)
split_int = int(split)

tip = tip_amount_int / 100
x = tip * bill_total_int
total_with_tip = x + bill_total_int
final_total = round(total_with_tip / split_int,2)

print(f"You should tip {x}")
print(f"Here is your total {final_total}")