import re

txt = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

txt2 = "32 * 698"
# Return a match at every white-space character:

print(len(txt))

x = re.findall("^[0-9]{1,4}\s[+-]\s[0-9]{1,4}$", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

x = re.findall("^[0-9]{1,4}\s[+-]\s[0-9]{1,4}$", txt2)

print(x)

line1 = ""
count = 1
txt = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
for x in txt:
    i = re.split("\s", x)
    if count < len(txt):
        line1 = line1 + ("    " + i[0])[-(len(max(i, key=len))+2):] + "    "
    else:
        line1 = line1 + ("    " + i[0])[-(len(max(i, key=len))+2):]
    count = count + 1
# print(line1)
count = 1
line2 = ""
for x in txt:
    i = re.split("\s", x)
    signo = i[1]
    if count < len(txt):
        line2 = line2 + signo + \
            ("    " + i[2])[-(len(max(i, key=len))+1):] + "    "
    else:
        line2 = line2 + signo + ("    " + i[2])[-(len(max(i, key=len))+1):]
        count = count + 1
# print(line2)

line = ""
line3 = ""
count = 1
for x in txt:
    line = ""
    i = len(max(re.split("\s", x), key=len))
    for y in range(i+2):
        line = line + "-"
    line3 = line3 + line + "    "
print(line1+"\n"+line2+"\n"+line3)

count = 1
line4 = ""
for x in txt:
    i = re.split("\s", x)
    if i[1] == "+":
        result = str(int(i[0]) + int(i[2]))
    else:
        result = str(int(i[0]) - int(i[2]))

    if count < len(txt):
        line4 = line4 + \
            ("         " + result)[-(len(max(i, key=len))+2):] + "    "
    else:
        line4 = line4 + ("         " + result)[-(len(max(i, key=len))+2):]
    count = count + 1


print(line4)

print(x[0])
print(x[2])
print("----")

if x[1] == "+":
    print(int(x[0]) + int(x[2]))
else:
    print(int(x[0]) - int(x[2]))
