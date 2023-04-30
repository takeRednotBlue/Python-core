import re
import random


# def find_all_phones(text):
#     pattern = re.compile(r"[+]380\(\d{2}\)\d{3}-((?P<first>\d{1})|(\d{2}))-(?(first)\d{3}|\d{2})")
#     # result = pattern.findall(text):
#     result = []
#     for match in pattern.finditer(text):
#         result.append(match.group())
#     return result

# test_text =  'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'

# print(find_all_phones(test_text))

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups= %r>' % (match.group(), match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
# a = displaymatch(valid.match("akt5q"))
# print(a)
# a = displaymatch(valid.match("akt5e"))
# print(a)
# a = displaymatch(valid.match("akt"))
# print(a)
# a = displaymatch(valid.match("727ak"))
# print(a)

"""Checking for a Pair"""
pair = re.compile(r".*(.).*\1")
# a = displaymatch(pair.match("717ak"))
# print(a)
# a = displaymatch(pair.match("718ak"))
# print(a)
# a = displaymatch(pair.match("354aa"))
# print(a)

"""Making a Phonebook"""

text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""

# entries = re.split("\n+", text)
# print(entries)

# phone_book_list = [re.split(":? ",  entry, 3) for entry in entries]

# print(phone_book_list)


"""Text Munging"""

# def repl(m):
#     inner_world = list(m.group(2))
#     random.shuffle(inner_world)
#     return m.group(1) + "".join(inner_world) + m.group(3)

# test = "Professor Abdolmaek, please report your absences promptly."
# a = re.sub(r"(\w)(\w+)(\w)", repl, test)
# print(a)

"""Finding all adverbs"""

# text = "He was carefully disguised but captured quickly by police."
# a = re.findall(r"\w+ly\b", text)
# print(a)

"""Finding all Adverbs and their Positions"""

# text = "He was carefully disguised but captured quickly by police."
# for m in re.finditer(r"\w+ly\b", text):
#     # print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
#     print('{:02d}-{:02d}: {}'.format(m.start(), m.end(), m.group(0)))


"""Writing a Tokenizer"""

from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',      r'\d+(\.\d*)?'),    # Integer or decimal number
        ('ASSIGN',      r':='),             # Assignment operator
        ('END',         r';'),              # Statement terminator
        ('ID',          r'[A-Za-z]+'),      # Identifiers
        ('OP',          r'[+\-*/]'),        # Arithmetic operators
        ('NEWLINE',     r'\n'),             # Line endings
        ('SKIP',        r'[ \t]+'),         # Skip over spaces and tabs
        ('MISMATCH',    r'.'),              # Any other character
    ] 
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} uexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = """
IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
"""
for token in tokenize(statements):
    print(token)
