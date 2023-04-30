# import decimal
import datetime


# name = "Fred"
# print(f"He said gis name is {name!r}")
# print(f"Ge said gis name is {repr(name)}")

# width = 10
# precision = 4
# value = decimal.Decimal("12.34567")
# print(f"result: {value:{width}.{precision}}")

# today = datetime.datetime(year=2023, month=4, day=27)
# print(f"{today:%B %d, %Y}")
# print(f"{today=:%B %d, %Y}")

# number = 1024
# print(f"{number:#0x}")

# foo = "bar"
# print(f"{foo = }")

# line = "The mill's is closed"
# print(f"{line = }")
# print(f"{line = :20}")
# print(f"{line = !r:20}")

"""
Formatting examples
"""

"""Aligning text and specifying a width"""

a = "{!r:<30}".format("left align")
print(repr(a))
b = "{:>30}".format("right align")
print(repr(b))
c = "{:^30}".format("centered")
print(repr(c))
d = "{:*^30}".format("centered") # use "*" as a fill char
print(repr(d))

"""Replacing %+f, %-f and % f and specifying a sign"""

a = "{:+f}; {:+f}".format(3.14, -3.14) # show it always
print(repr(a))
b = "{: f}' {: f}".format(3.14, -3.14) # show a space for positive numbers
print(repr(b))
c = "{:-f}; {:-f}".format(3.14, -3.14) # show only the minus --  same as "{:f}; {:f}"
print(repr(c))

"""Replacing %x and %o and converting the value to different bases"""
# format also supports binary numbers
a = "int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42)
print(repr(a))
# with 0x, 0o, or 0b as prefix
b = "int: {0:#d}; hex: {0:#X}; oct: {0:#o}; bin: {0:#b}".format(42)
print(repr(b))

"""Using coma as thousands separator"""

a = "{:,}".format(1234567890)
print(repr(a))

"""Expressing a percentage"""

points = 19
total = 22
result = "Correct answers: {:.2%}".format(points/total)
print(repr(result))

"""Using type-specific formatting"""

d = datetime.datetime(2023, 4, 25, 23, 35, 20)
a = "{:%Y-%m-%d %H:%M:%S}".format(d)
print(repr(a))

"""Nesting arguments and more complex examples"""

for align, text in zip('<^>', ['left', 'center', 'right']):
    a = "{0:{fill}{align}16}".format(text, fill=align, align=align)
    print(a)

octets = [192, 168, 0, 1]
a = '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
print(a)

width = 5

for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()


