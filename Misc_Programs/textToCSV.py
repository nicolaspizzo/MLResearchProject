import csv

def removeSpace(string):
  if (string[0] == " "):
    return string[1:]
  else:
    return string


f = open("Questions.txt", "r")
lines = f.readlines()

columns = ['Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Answer 5', 'Explanation', 'Author']
rows = []

#Iterate through all lines
for i in range (0, len(lines)):
  if (len(lines[i]) > 2):
    if (lines[i][0:2] == "ID"):
      i += 2
      singleRow = []
      singleRow.append(removeSpace(lines[i]))
      i = i + 1
      if (lines[i][0:1] == "*"):
        singleRow.append(removeSpace(lines[i][3:]))
        i = i + 1
      else:
        singleRow.append(removeSpace(lines[i][2:]))
        i = i + 1
      if (lines[i][0:1] == "*"):
        singleRow.append(removeSpace(lines[i][3:]))
        i = i + 1
      else:
        singleRow.append(removeSpace(lines[i][2:]))
        i = i + 1
      if (lines[i][0:1] == "*"):
        singleRow.append(removeSpace(lines[i][3:]))
        i = i + 1
      else:
        singleRow.append(removeSpace(lines[i][2:]))
        i = i + 1
      if (lines[i][0:1] == "*"):
        singleRow.append(removeSpace(lines[i][3:]))
        i = i + 1
      else:
        singleRow.append(removeSpace(lines[i][2:]))
        i = i + 1
      if (lines[i][0:2] == "e)"):
        singleRow.append(removeSpace(lines[i][2:]))
        i = i + 1
      elif (lines[i][0:3] == "*e)"):
        singleRow.append(removeSpace(lines[i][3:]))
      else:
        singleRow.append("")
      if (lines[i][0:11] == "Explanation"):
        singleRow.append(lines[i][13:])
        rows.append(singleRow)
        i = i + 1
      else:
        singleRow.append("")
      if (lines[i][0:6] == "Author"):
        singleRow.append(lines[i][8:])
        rows.append(singleRow)
        i = i + 1
      else:
        singleRow.append("")

with open('Questions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for i in range (0, len(rows)):
      writer.writerow(rows[i])