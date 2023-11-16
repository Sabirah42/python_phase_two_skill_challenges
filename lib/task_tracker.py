def task_tracker(text):
    if text == "":
        raise Exception("Input value must not be empty")

    if "#TODO" in text:
        return "This is a task"
    else:
        return "This is not a task"