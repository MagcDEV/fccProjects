def arithmetic_arranger(problems, solution=False):
    #### PRUEBAS #######################################################
    import re
    if len(problems) > 5:
        return "Error: Too many problems."

    for x in problems:
        if not (re.findall("[+|-]", x)):
            return "Error: Operator must be '+' or '-'."
        elif (re.findall("[a-zA-Z]", x)):
            return "Error: Numbers must only contain digits."
        elif (re.findall("[0-9]{5,}", x)):
            return "Error: Numbers cannot be more than four digits."
    ####################################################################
    line1 = ""
    count = 1
    for x in problems:
        i = re.split("\s", x)
        if count < len(problems):
            line1 = line1 + \
                ("     " + i[0])[-(len(max(i, key=len))+2):] + "    "
        else:
            line1 = line1 + ("     " + i[0])[-(len(max(i, key=len))+2):]
        count = count + 1

    count = 1
    line2 = ""
    for x in problems:
        i = re.split("\s", x)
        signo = i[1]
        if count < len(problems):
            line2 = line2 + signo + \
                ("     " + i[2])[-(len(max(i, key=len))+1):] + "    "
        else:
            line2 = line2 + signo + \
                ("      " + i[2])[-(len(max(i, key=len))+1):]
        count = count + 1

    line = ""
    line3 = ""
    count = 1
    for x in problems:
        line = ""
        i = len(max(re.split("\s", x), key=len))
        for y in range(i+2):
            line = line + "-"
        if count < len(problems):
            line3 = line3 + line + "    "
        else:
            line3 = line3 + line
        count = count + 1

    count = 1
    line4 = ""
    for x in problems:
        i = re.split("\s", x)
        if i[1] == "+":
            result = str(int(i[0]) + int(i[2]))
        else:
            result = str(int(i[0]) - int(i[2]))

        if count < len(problems):
            line4 = line4 + \
                ("         " + result)[-(len(max(i, key=len))+2):] + "    "
        else:
            line4 = line4 + ("         " + result)[-(len(max(i, key=len))+2):]
        count = count + 1

    if solution:
        arranged_problems = line1+"\n"+line2+"\n"+line3+"\n"+line4
    else:
        arranged_problems = line1+"\n"+line2+"\n"+line3

    return arranged_problems


print(arithmetic_arranger(
    ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
