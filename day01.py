input_data = open("input/day01.txt").read()

elves_stock = [list(map(int, stock_list.split('\n'))) for stock_list in input_data.split('\n\n')]
elves_calories = [sum(stock) for stock in elves_stock]
sorted_elves_calories = sorted(elves_calories, reverse=True)

print(f"Part One: {sorted_elves_calories[0]}")
print(f"Part Two: {sum(sorted_elves_calories[0:3])}")
