letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open("./Day3/input.txt") as f:
    data = f.read()
    data = data.split()
    priorities = 0
    for i in data:
      section1 = i[0:(len(i) // 2)]
      section2 = i[(len(i) // 2):len(i)]
      common_char = list(set(section1) & set(section2))
      priorities += (letters.index(common_char[0]) + 1)
    print(priorities) 