def arithmetic_arranger(problems, solutions=False):

    l = len(problems)

    if l > 5:
        return "Error: Too many problems."

    top = list()
    sym = list()
    bot = list()
    space = list()

    for entry in problems:
        parts = entry.split()

        # Checking for errors
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if parts[1] != "+" and parts[1] != "-":
            return "Error: Operator must be '+' or '-'."
        try:
            int(parts[0])
        except:
            return "Error: Numbers must only contain digits."

        try:
            int(parts[2])
        except:
            return "Error: Numbers must only contain digits."

        top.append(parts[0])
        sym.append(parts[1])
        bot.append(parts[2])
        space.append(len(max(parts, key=len)) + 2)

    # sol = [str(int(x) + int(y)) for x, y in zip(top, bot)]
    sol = list()
    for i in range(l):
        if sym[i] == "+":
            sol.append(str(int(top[i]) + int(bot[i])))
        if sym[i] == "-":
            sol.append(str(int(top[i]) - int(bot[i])))

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
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    if not solutions:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43',
                           '123 + 49', '988 + 40'], True))
