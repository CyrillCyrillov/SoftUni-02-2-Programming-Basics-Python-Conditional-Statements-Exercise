budget = float(input())
mutes = int(input())
price_for_one_dress = float(input())
price_for_decor = budget * 0.1
if mutes > 150:
    sum = (mutes * price_for_one_dress * 0.9) + price_for_decor
else:
    sum = mutes * price_for_one_dress + price_for_decor

if sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - sum:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {sum - budget:.2f} leva more.")


