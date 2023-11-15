import math

def text_reader(text):
    text_length = len(text.split())

    if text_length >= 200:
        num_mins = int(math.ceil(text_length/200))
        print(f"It would take you {num_mins} minutes to read this text.")
        return f"It would take you {num_mins} minutes to read this text."