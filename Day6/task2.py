with open("./day6/input.txt") as f:
  datastream = f.read()
  for i in range(14, len(datastream)):
    if (len(set(datastream[i-14:i])) == len(datastream[i-14:i])):
      print(i)
      break