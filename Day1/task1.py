with open('./day1/input.txt') as f:
    data = f.read().split('\n\n')
    
    total_calories = []
    for i in range(len(data)):
      data[i] = data[i].split('\n')
    for i in range(len(data)):
      sum_calories = 0
      for j in range(len(data[i])):
        sum_calories = sum_calories + int(data[i][j])
      total_calories.append(sum_calories)

total_calories.sort()
print(total_calories[-1])

