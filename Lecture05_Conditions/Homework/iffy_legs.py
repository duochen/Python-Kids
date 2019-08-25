has_zero_legs = 0
has_two_legs = 0
has_four_legs = 0

animals = [4, 0, 2, 4, 2, 0, 2, 4, 4, 2, 0, 2, 4]
for i in range(len(animals)):
    if animals[i] == 0:
        has_zero_legs += 1
    elif animals[i] == 2:
        has_two_legs += 1
    elif animals[i] == 4:
        has_four_legs += 1
animal_summary = f'''
Animals with no legs: {has_zero_legs}
Animals with two legs: {has_two_legs}
Animals with four legs: {has_four_legs}
'''
print(animal_summary)
