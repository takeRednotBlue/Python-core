
def commands_parser(input: str) -> tuple:
    # hello *args(ignore)
    # add <name> <phone> *args(ignore)
    # change <name> <phone> *args(ignore)
    # phone <name> *args(ignore)
    # show all *args(ignore)
    # good bye|close|exit *args(ignore)
    # help *args(ignore)
    words_list = input.split()
    if words_list[0].lower() == 'show' or words_list[0].lower() == 'good':
        command = ' '.join(words_list[:2]).lower()
        arguments = words_list[2:]
    else:
        command = words_list[0].lower()
        arguments = words_list[1:]
    
    return command, arguments