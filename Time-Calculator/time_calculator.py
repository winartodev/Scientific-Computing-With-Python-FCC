def add_time(start, duration, day=""):   
    day_of_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split duartion
    split_duration = duration.partition(":")
    # Get Duration Hours
    duration_hours = int(split_duration[0])
    # Get Duration Minutes
    duration_minutes = int(split_duration[2])

    # Split Start Time
    split_start = start.partition(":")
    # Get Start Hours
    start_hours = int(split_start[0])
    # Get Start Minutes
    start_minutes = int(split_start[2].partition(" ")[0])
    # Get AM or PM
    am_or_pm = split_start[2].partition(" ")[2] # AM
    # fip am or pm
    am_or_pm_flip = {'AM':'PM', 'PM':'AM'}

    total_minutes = int(start_minutes + duration_minutes)

    ammount_of_days = int(duration_hours / 24)

    if total_minutes > 60:
        start_hours += 1
        total_minutes = total_minutes % 60
    
    ammount_of_am_pm = int((start_hours + duration_hours) / 12) % 2
    
    total_hours = int(start_hours + duration_hours) % 12

    total_hours = total_hours = 12 if total_hours == 0 else total_hours

    total_minutes = total_minutes if total_minutes > 9 else "0" + str(total_minutes)
   
    if am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        ammount_of_days += 1

    am_or_pm = am_or_pm_flip[am_or_pm] if ammount_of_am_pm == 1 else am_or_pm

    new_time = str(total_hours) + ":" + str(total_minutes) + " " + str(am_or_pm) 
    
    if (day):
        day = day.lower()
        index = int(day_of_week_index[day] + ammount_of_days) % 7
        new_time += ', ' + day_of_week[index]

    if ammount_of_days == 1:
        return new_time + " (next day)"
    elif ammount_of_days > 1:
        return new_time + f" ({ammount_of_days} days later)"
        
    return new_time