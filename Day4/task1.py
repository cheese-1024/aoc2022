with open("./day4/input.txt") as f:
  data = [line.split(",") for line in f]
  fully_contained = 0
  for i in range(len(data)):
    for j in range(len(data[i])):
      data[i][j] = data[i][j].strip()
  for i in range(len(data)):
    elf1num1 = ""
    elf1num2 = ""
    elf2num1 = ""
    elf2num2 = ""
    for j in range(len(data[i])):
      second = False
      for char in data[i][j]:
        if j == 0:
          if char.isdigit() and second == False:
            elf1num1 += char
          elif char.isdigit() == False:
            second = True
          if char.isdigit() and second == True:
            elf1num2 += char
        elif j == 1:
          if char.isdigit() and second == False:
            elf2num1 += char
          elif char.isdigit() == False:
            second = True
          if char.isdigit() and second == True:
            elf2num2 += char
      if elf1num1 != "" and elf1num2 != "" and elf2num1 != "" and elf2num2 != "":
        if int(elf1num1) >= int(elf2num1) and int(elf1num2) <= int(elf2num2):
          fully_contained += 1
        elif int(elf2num1) >= int(elf1num1) and int(elf2num2) <= int(elf1num2):
          fully_contained += 1
print(fully_contained)