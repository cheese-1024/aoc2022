with open("./day6/input.txt") as f:
  datastream = f.read()
  for i in range(4, len(datastream)):
    if (len(set(datastream[i-4:i])) == len(datastream[i-4:i])):
      print(i)
      break