def task_tracker(text):
    is_string = isinstance(text, str)

    if text == "":
        raise Exception("Input value must not be empty")
    elif is_string == False:
        raise Exception("Input value must be a string")

    if "#TODO" in text:
        return "This is a task"
    else:
        return "This is not a task"