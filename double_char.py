while True:
    strings = input()

    if strings == "End":
        break

    if strings != "SoftUni":
        doubled_string = ""
        for char in strings:
            doubled_string += 2 * char
        print(doubled_string)