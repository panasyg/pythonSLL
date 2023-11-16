import random

characters = {
    'a': [
        '  A  ',
        ' A A ',
        'AAAAA',
        'A   A',
        'A   A',
    ],
    'b': [
        'BBBB ',
        'B   B',
        'BBBB ',
        'B   B',
        'BBBB ',
    ],
    'c': [
        ' CCCC',
        'C    ',
        'C    ',
        'C    ',
        ' CCCC',
    ],
    'd': [
        'DDDD ',
        'D   D',
        'D   D',
        'D   D',
        'DDDD ',
    ],
    # Додайте інші літери за аналогією
}

color_options = {
    '1': 'black-white',
    '2': 'gray shades',
    '3': 'custom color',  # Додайте власні кольори за бажанням
}

alignment_options = {
    '1': 'left',
    '2': 'center',
    '3': 'right',
}

def get_user_input():
    input_text = input("Enter the text for ASCII art: ")
    return input_text

def get_alignment():
    print("Choose alignment:")
    for key, value in alignment_options.items():
        print(f"{key}: {value}")
    alignment_choice = input("Enter the number: ")
    return alignment_options.get(alignment_choice, 'left')

def get_art_size():
    while True:
        try:
            width = int(input("Enter the width of ASCII art: "))
            height = int(input("Enter the height of ASCII art: "))
            return width, height
        except ValueError:
            print("Please enter valid values for size.")

def choose_color_option():
    print("Choose color option:")
    for key, value in color_options.items():
        print(f"{key}: {value}")
    color_choice = input("Enter the number: ")
    return color_options.get(color_choice, 'black-white')

def generate_ascii_art(input_text, characters, alignment, width, height, color_option):
    lines = []

    if alignment == 'center':
        lines.append(input_text.center(width))
    elif alignment == 'right':
        lines.append(input_text.rjust(width))
    else:
        lines.append(input_text.ljust(width))

    for i in range(5):  # Assuming each character has 5 lines
        line = ""
        for char in input_text.lower():
            if char in characters:
                line += characters[char][i]
            else:
                line += " " * 6  # Spaces if the character is not found
            line += " "  # Additional space between characters

        if color_option == 'black-white':
            line = "\033[30m" + line + "\033[0m"  # Black color for text
        elif color_option == 'gray shades':
            line = "\033[90m" + line + "\033[0m"  # Gray color for text
        elif color_option == 'custom color':
            # Додайте ваші власні кольори та їх коди тут
            custom_color_code = input("Enter the custom color code: ")
            line = f"\033[{custom_color_code}m" + line + "\033[0m"

        lines.append(line)

    return lines

def preview_ascii_art(art):
    print("Preview of ASCII art:")
    for line in art:
        print(line)

def save_ascii_art(art):
    save_option = input("Do you want to save ASCII art to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter the filename: ")
        with open(filename, 'w') as file:
            for line in art:
                file.write(line + '\n')

def main():
    input_text = get_user_input()
    alignment = get_alignment()
    width, height = get_art_size()
    color_option = choose_color_option()

    art = generate_ascii_art(input_text, characters, alignment, width, height, color_option)

    for line in art:
        print(line)

    preview_option = input("Do you want to see a preview of the ASCII art? (yes/no): ").lower()
    if preview_option == 'yes':
        preview_ascii_art(art)

    save_ascii_art(art)

if __name__ == "__main__":
    main()
