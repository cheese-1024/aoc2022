crates = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'], ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'], ['G', 'F', 'Q', 'T', 'S', 'L', 'B'], ['L', 'G', 'C', 'Z', 'V'], ['N', 'L', 'G'], ['J', 'F', 'H', 'C']]

with open("./day5/movements.txt") as f:
  movements_list = [movement.replace("move ", "").replace(" from", "").replace(" to", "").split(" ") for movement in f.read().splitlines()]

  for i in range(len(movements_list)):
    src = (int(movements_list[i][1]) - 1)
    qty = ((int(movements_list[i][0])))
    dst = (int(movements_list[i][2])-1)
    for _ in range(qty):
      crates[dst].append(crates[src].pop())

  print(''.join((s[-1] for s in crates)))

