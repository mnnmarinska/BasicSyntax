n = int(input())

for inputs in range(n):
    string_to_check = input()
    if "," in string_to_check or "." in string_to_check or "_"in string_to_check:
        print(f"{string_to_check} is not pure!")
    else:
        print(f"{string_to_check} is pure.")