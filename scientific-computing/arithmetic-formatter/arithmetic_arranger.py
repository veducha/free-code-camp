def arithmetic_arranger(problems):
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

    print(top, sym, bot, space)
    return None


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
