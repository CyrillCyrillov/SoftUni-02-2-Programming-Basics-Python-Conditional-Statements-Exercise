number = float(input())
input_unit = input()
output_unit = input()
if input_unit == "m":
    if output_unit == "cm":
        print(f"{number * 100:.3f}")
    elif output_unit == "mm":
        print(f"{number * 1000:.3f}")
    else:
        print(number)
if input_unit == "cm":
    if output_unit == "m":
        print(f"{number / 100:.3f}")
    elif output_unit == "mm":
        print(f"{number * 10:.3f}")
    else:
        print(number)
if input_unit == "mm":
    if output_unit == "cm":
        print(f"{number / 10:.3f}")
    elif output_unit == "m":
        print(f"{number / 1000:.3f}")
    else:
        print(number)
