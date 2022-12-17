letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open("./input3.txt") as f:
  data = f.read().split()
  print(data)
  total = 0
  for i in range(0, len(data), 3):
    sameChar = list(set(data[i]) & set(data[i+1]) & set(data[i+2]))
    total += (letters.index(sameChar[0]) + 1)
  print(total)