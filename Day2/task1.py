with open("./input2.txt") as f:
  game = f.read().split()
  score = 0
  for i in range(0, len(game), 2):
    if game[i] == "A" and game[i+1] == "X":
      score += 4
    elif game[i] == "A" and game[i+1] == "Y":
      score += 8
    elif game[i] == "A" and game[i+1] == "Z":
      score += 3
    elif game[i] == "B" and game[i+1] == "X":
      score += 1
    elif game[i] == "B" and game[i+1] == "Y":
      score += 5
    elif game[i] == "B" and game[i+1] == "Z":
      score += 9
    elif game[i] == "C" and game[i+1] == "X":
      score += 7
    elif game[i] == "C" and game[i+1] == "Y":
      score += 2
    elif game[i] == "C" and game[i+1] == "Z":
      score += 6
print(score)