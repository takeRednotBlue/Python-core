# def sanitize_phone_number(phone):
#     san_phone_number = ""
#     for char in phone:
#         if char.isnumeric():
#             san_phone_number += chr
#     return san_phone_number

def sanitize_phone_number(phone):
    invalid_char = {"(", "-", ")", "+", " "}
    normalize_list = list(phone)
    for char in normalize_list:
        if char in invalid_char:
            normalize_list.remove(char)
    return "".join(normalize_list)

test =  "38050 111 22 11   "
phone = sanitize_phone_number(test)

print(phone)
print(len(phone))
print(len("380501112211"))