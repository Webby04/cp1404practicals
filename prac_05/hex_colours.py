"""
CP1404/CP5632 Practical
Hex colour in a dictionary
"""

NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "burnt orange": "#cc5500",
                "cobalt": "#0047ab", "coffee": "#6f4e37", "electric lime": "#ccff00", "harvest gold": "#da9100",
                "iris": "#6f4e37", "lavender": "#e6e6fa", "magenta": "#ff00ff"}
print(NAME_TO_CODE)

colour_code = input("Enter colour: ").lower()
while colour_code != "":
    print(f"The colour code of {colour_code} is {NAME_TO_CODE[colour_code]}")
    print("Invalid colour")
    colour_code = input("Enter colour: ").lower()
