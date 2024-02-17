import re
from datetime import datetime

def read_file_to_string(fileName: str):
    try:
        with open(fileName, mode='r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
        return None
    finally:
        file.close()


filename: str = "text3.txt"

file_content = read_file_to_string(filename)

text = file_content[100:302]
print("Part of the text, received from file:\n")
print("'" + text + "'\n")

print("Text properties:")
print("length: ", len(text))
print("Count of 't' letters: ", text.count('t'))
print("Index of 's' letter: ", text.find('s'))
print("Index where 'seed' substring starts: ", text.index("ceed"))
print("\nCapitalized text: ", text.capitalize())
print("\nText in upper case: ", text.upper())
print("\nText in lower case: ", text.lower())
print("\nTitle text: ", text.title())
print("\nJoined text: ", "-".join(text))

print("Other methods:\n")
print("Text is alpha: ", text.isalpha())
print("Text is digit: ", text.isdigit())
print("Text[1:2] is alphanumeric: ", text[1:3].isalnum())
print("Text is lower: ", text.islower())
print("Text is upper: ", text.isupper())
print("Text is title: ", text.istitle())
print("Text is space: ", text.isspace())
print("Text starts with '(': ", text.startswith("("))
print("Text ends with ' ': ", text.endswith(" "))

print("\nText split by ' ': ", text.split(" "))
print("\nText replace ' ': ", text.replace(" ", "_"))

date_pattern = re.compile(r'\b((0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}|\d{4}-\d{2}-\d{2})\b')

# Знаходимо всі дати у тексті
dates = date_pattern.findall(file_content)
print("\nDates in the text:", [date[0] for date in dates])

formatted_dates = []
for date in dates:
    # Використовуємо datetime для переведення у зазначений формат
    date_obj = datetime.strptime(date[0], "%m/%d/%Y" if '/' in date[0] else "%Y-%m-%d")
    formatted_date = date_obj.strftime("%Y-%m-%d")
    formatted_dates.append((date[0], formatted_date))

# Замінюємо всі дати у тексті на переведені у формат "%Y-%m-%d"
for old_date, new_date in formatted_dates:
    file_content = file_content.replace(old_date, new_date)

print("\nText with replaced dates\n\n" + file_content)