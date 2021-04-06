str = "CYP3A4 (cytochrome P450 family 3 subfamily A member 4)"

a = str.split("(")

b = "("+a[-1]

c = b.split(")")

if (c[1].isspace()) or (not c[1]):
    print(c[0] + ")")
else:
    print(c[1], ": contains digits and/or num values.")


print(len(c[1]))

