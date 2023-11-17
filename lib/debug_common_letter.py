def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        # print(counter)
        
    letter = sorted(counter.items(), key=lambda item: item[1])[-2][0]
    # print(sorted(counter.items(), key=lambda item: item[1]))
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")