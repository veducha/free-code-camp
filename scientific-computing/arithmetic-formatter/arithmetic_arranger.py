def arithmetic_arranger(problems, solutions=False):
    l = len(problems)

    top = list()
    sym = list()
    bot = list()
    space = list()

    for entry in problems:
        parts = entry.split()

        top.append(parts[0])
        sym.append(parts[1])
        bot.append(parts[2])
        space.append(len(max(parts, key=len)) + 2)

    sol = [str(int(x) + int(y)) for x, y in zip(top, bot)]

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(l):
        line1 += top[i].rjust(space[i], " ")
        line2 += sym[i] + bot[i].rjust(space[i]-1, " ")
        line3 += "".rjust(space[i], "-")
        line4 += sol[i].rjust(space[i], " ")

        if i < l-1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "

    # print(line1)

    if solutions:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    if not solutions:
        return line1 + "\n" + line2 + "\n" + line3
