import re

pattern = input("Enter regex pattern: ")
text = input("Enter test text: ")

try:
    matches = re.findall(pattern, text)

    if matches:
        print("\nMatches:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")

except re.error:
    print("Invalid regex pattern.")
