income = float(input())
average_success = float(input())
minimal_salary = float(input())
social_scholarship = 0
success_scholarship = 0
import math
if (income < minimal_salary) & (average_success > 4.5):
    social_scholarship = math.floor(minimal_salary * 0.35)
if average_success >= 5.5:
    success_scholarship = math.floor(average_success * 25)
if (social_scholarship > 0) & (success_scholarship > 0):
    if success_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {success_scholarship} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship} BGN")
elif social_scholarship > 0 & success_scholarship == 0:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif success_scholarship > 0 & social_scholarship == 0:
    print(f"You get a scholarship for excellent results {success_scholarship} BGN")
else:
    print("You cannot get a scholarship!")
