def timeConversion(s):
    meridian = s[-2:]
    hour = int(s[:2])
    
    if meridian == "PM" and hour != 12:
        hour += 12
    elif meridian == "AM" and hour == 12:
        hour = 0
        
    return f"{hour:02d}{s[2:-2]}"
