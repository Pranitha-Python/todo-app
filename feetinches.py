from parsers import parse

feet_inches = input("Enter feet and inches:")


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']}  feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("kid is too small")
else:
    print("kid can use the slide")

