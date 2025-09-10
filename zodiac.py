zodiac_animals=["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Hare","Dragon","Snake","Horse","Goat"]
while True:
    your_year=input('Enter a year:')
    if not your_year.isdigit():
        print('invalid, please enter a non negative integer')
        continue
    year=int(your_year)
    if year<0:
        print('Input positive year')
        continue
    animal_index=year%12
    animal=zodiac_animals[animal_index]
    print(f"The year of {year} is the animal of {animal}")
    break
