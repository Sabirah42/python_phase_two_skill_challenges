import math

def text_reader(text):
    is_string = isinstance(text, str)

    if is_string == False:
        raise Exception("Input value must be a string")
    
    text_length = len(text.split())

    if text == '':
        print("It would take you 0 minutes to read this text.")
        return "It would take you 0 minutes to read this text."

    elif text_length >= 200:
        num_mins = int(math.ceil(text_length/200))
        print(f"It would take you {num_mins} minutes to read this text.")
        return f"It would take you {num_mins} minutes to read this text."

    else:
        print("It would take you less than 1 minute to read this text.")
        return "It would take you less than 1 minute to read this text."