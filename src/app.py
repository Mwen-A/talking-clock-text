from handlers import reformat_time, sentence_construction, set_current_time
import re
import argparse


def with_user_input(user_time: str) -> str:
    """Accepts time as a user input and returns the time in 'human-friendly' text
    as a multiple of five. With incorrect input it returns a string describing the accepted format

    Parameters: Time in the format HH:MM
    Returns: The time in 'human-friendly' text or formatting suggestions

    """
    validation = re.fullmatch(r"(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]", user_time)
    if validation:
        updated_time = reformat_time(user_time)
        return sentence_construction(updated_time).capitalize()
    else:
        return 'Incorrect time format - use HH:MM, 24h format with 00:00 as midnight'


def no_user_input() -> str:
    """Gets the current time, sets the minutes as a multiple of five
    and returns the time in 'human-friendly' text

    Returns: The time in 'human-friendly' text

    """
    current_time = set_current_time()
    updated_time = reformat_time(current_time)
    return sentence_construction(updated_time).capitalize()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='app')
    parser.add_argument('settime', type=str, nargs='?', help="Input from user in the HH:MM format", action='store')
    args = parser.parse_args()
    if args.settime:
        print(with_user_input(args.settime))
    else:
        print(no_user_input())
