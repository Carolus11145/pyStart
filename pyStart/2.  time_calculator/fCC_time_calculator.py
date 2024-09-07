def add_time(start, duration, day=""):
    # Variables which are to serve as the bases of the return values
    week_ds = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    start_hr = int(start.split(' ')[0].split(':')[0]) # Separates first 2 digits of starting time and converts them to integers
    start_min = int(start.split(' ')[0].split(':')[1]) # Separates last 2 digits of starting time and converts them to integers
    dur_hr = int(duration.split(":")[0]) # Separates first digits of duration time and converts them to integers
    dur_min = int(duration.split(":")[1]) # Separates last two digits of duration time and converts them to integers
    noon = start.split(" ")[1] # Separates the PM/AM section of the starting time 

    # Below is the code to calculate the totals of times
    if noon == "PM" : # Conditional which adds the necessary int obj to the starting hour
        start_hr += 12
    
    end_hr = start_hr + dur_hr + ((start_min + dur_min) // 60)
    end_min = (start_min + dur_min) %  60

    # FInal hours for the 12 Hour format which is to be used
    final_hr = (end_hr % 24) % 12
    if final_hr == 0:
        final_hr = 12
    final_hr = str(final_hr)

    # Total days which will display with the new time
    final_d = (end_hr // 24) 
    
    # Code for formatting the morning and noon hours
    if (end_hr % 24) <= 11:
        noon = "AM"
    else:
        noon = "PM"

    #Single digit minutes format
    if end_min < 10:
        final_min = "0" + str(end_min)
    else:
        final_min = str(end_min)

    new_time = f"{final_hr}:{final_min} {noon}" # Variable stores the final time which will be returned by the fn

    #Final edits for returning desired time format
    if day == "":
        if final_d == 0:
            return new_time
        if final_d == 1:
            return f"{new_time} (next day)"
        return f"{new_time} ({str(final_d)} days later)"
    else:
        final_week_d = (week_ds[day.lower().capitalize()] + final_d) % 7
        for x, y in week_ds.items():
            if y == final_week_d:
                final_week_d = x
                break
        if final_d == 0:
            return f'{new_time}, {final_week_d}'
        if final_d == 1:
            return f"{new_time}, {final_week_d} (next day)"
        return f"{new_time}, {final_week_d} ({str(final_d)} days later)"
        
print(add_time("8:16 PM", "466:02"))
