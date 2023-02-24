# dictionary to convert day to number
days = {
    'sunday': 0,
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6
}


# input
while True:
    day_start = input("Your vacation start day: ").strip().lower()
    if len(day_start) > 10:
        print("Make it shorter. Your input length is ", str(len(day_start)))
    else:
        break
duration = int(input("How long is your vacation: "))


for key in days:
    if key == day_start:
        day_start = days[key]   # set the start day to value for calculations
        break

end_day = day_start + (duration % 7)

for key, value in days.items():
    if end_day == value:
        end_day = key   # set the return day to key for printing
        break

print("Your comeback day is: ", str(end_day))
