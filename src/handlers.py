from datetime import datetime


def set_current_time() -> str:
    """Returns the current time in the format HH:MM

    Returns: Time in the format HH:MM

    """
    current_time = datetime.now().strftime("%H:%M")
    return current_time


def reformat_time(current_time: str) -> str:
    """Modifies the minutes in the timestamp to a multiple of five

    Parameters: Time in the format HH:MM
    Returns: Time in the format HH:MM with :MM divisible by five 

    """
    minutes = current_time[-2:]
    minutes_in_five = "%02d" % (5 * round(int(minutes) / 5))
    current_time_list = list(current_time)
    current_time_list[-2:] = minutes_in_five
    updated_time = ''.join(current_time_list)
    return updated_time


def sentence_construction(updated_time: str) -> str:
    """Converts the time to human-friendly text

    Parameters: Time in the format HH:MM with minutes divisible by 5
    Returns: Time in human-friendly text

    """
    minutes = int(updated_time[-2:])
    if minutes > 30:
        hrs = int(updated_time[:2]) + 1
    elif minutes <= 30 and minutes >= 0:
        hrs = int(updated_time[:2]) 
    if hrs > 12 or hrs == 00:
        hrs -= 12
        hrs = abs(hrs)
    if minutes == 0:
        sentence = hours_dict[hrs] + minutes_dict[minutes]
    else:
        sentence = minutes_dict[minutes] + hours_dict[hrs]
    return sentence


hours_dict = {1: 'one', 2: 'two', 3: 'three',
            4: 'four', 5: 'five', 6: 'six',
            7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve'}


minutes_dict = {0: " o'clock", 5: 'five past ', 10: 'ten past ',
        15: 'quarter past ', 20: 'twenty past ', 25: 'twenty five past ', 
        30: 'half past ', 35: 'twenty five to ', 40: 'twenty to ', 
        45: 'quarter to ', 50: 'ten to ', 55: 'five to '}
