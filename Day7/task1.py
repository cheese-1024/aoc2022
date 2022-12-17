with open("./day7/input.txt") as f:
  terminal = f.read().split("\n")
  print(terminal)
  level = 0
  dirs = []
  dir = ""
  repetitions = 0
  terminal.pop(0)
  for command in terminal:
    if command.startswith("$ cd") and command.endswith(".."):
      level -= 1
    elif command.startswith("$ cd") and (not command.endswith("..")):
      level += 1
    
    if level != 0 or repetitions == 0:
      for char in command:
        if char.isdigit():
          dir += char
    if dir is not "" and level == 0:
      dirs.append(dir)
      dir = ""
  repetitions += 1
  for x in dirs:
      if int(x) >= 100000:
        dirs.remove(x)
  print(sum(int(x) for x in dirs))
