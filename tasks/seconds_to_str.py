__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    # there are 86400 sec in a day
    seconds = seconds
    minute = 60
    hour = 60 * minute
    day = hour * 24

    days = seconds // day   
    hours = (seconds - (days * day)) // hour
    minutes = (seconds - ((days * day) + (hours * hour))) // minute
    seconds_left = seconds % minute
    
    # part that prints result and formants it
    if days:
        return f'{days:02d}d{hours:02d}h{minutes:02d}m{seconds_left:02d}s'
    elif hours:
        return f'{hours:02d}h{minutes:02d}m{seconds_left:02d}s'
    elif minutes:
        return f'{minutes:02d}m{seconds_left:02d}s'
    else:
        return f'{seconds_left:02d}s'
        
print(seconds_to_str(5))