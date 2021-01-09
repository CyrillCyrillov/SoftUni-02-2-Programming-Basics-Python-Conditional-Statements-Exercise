world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())
import math
time = seconds_per_meter * distance + math.floor(distance / 15) * 12.5
if time < world_record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - world_record:.2f} seconds slower.")
