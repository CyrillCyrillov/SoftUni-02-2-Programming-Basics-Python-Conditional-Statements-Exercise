hour = int(input())
minutes = int(input())
minutes += 15
if minutes >= 60:
    hour += 1
    minutes -= 60
if hour > 23:
    hour = 0
if minutes < 9:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")

