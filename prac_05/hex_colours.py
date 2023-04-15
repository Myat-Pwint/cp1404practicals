COLOURS = {"AliceBlue": "#F0F8FF", "Aquamarine": "#7FFFD4", "Beige": "#F5F5DC", "Coral": "#FF7F50", "DarkOrange": "#FF8C00",
                "Fuchsia": "#FF00FF", "Gold": "#FFD700", "Indigo": "#4B0082", "Magenta": "#FF00FF", "Plum": "#DDA0DD"}
print(COLOURS)

color_name = input("Enter color name: ").upper()
while color_name != "":
    if color_name in COLOURS:
        print(f"{color_name} is {COLOURS[color_name]}")
    else:
        print("Invalid color code!")
    color_name = input("Enter color name: ").upper()

for color, name in COLOURS.items():
    print(f"{color} is {name}")
