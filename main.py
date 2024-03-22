# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
date = input("Enter today's date:")
mood = input("How are you today? on the scale of 1 to 10: ")
thoughts = input("let your thoughts flow:\n")
with open(f"journal\{date}.txt","w") as file:
     file.write(mood + 2 * "\n")
     file.write(thoughts)
