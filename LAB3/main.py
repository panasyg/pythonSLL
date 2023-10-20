import pyfiglet
from termcolor import colored

class ASCIIGenerator:
    def get_user_input(self):
        self.text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")

    def select_font(self):
        fonts = pyfiglet.FigletFont.getFonts()
        print("Доступні шрифти:")
        for i, font in enumerate(fonts, start=1):
            print(f"{i}. {font}")
        while True:
            try:
                selected_font = int(input("Оберіть номер шрифту: "))
                if 1 <= selected_font <= len(fonts):
                    return fonts[selected_font - 1]
                else:
                    print("Недійсний ввід. Введіть правильний номер шрифту.")
            except ValueError:
                print("Недійсний ввід. Введіть правильний номер шрифту.")

    def select_color(self):
        colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
        print("Доступні кольори:")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")
        while True:
            try:
                selected_color = int(input("Оберіть номер кольору: "))
                if 1 <= selected_color <= len(colors):
                    return colors[selected_color - 1]
                else:
                    print("Недійсний ввід. Введіть правильний номер кольору.")
            except ValueError:
                print("Недійсний ввід. Введіть правильний номер кольору.")

    def choose_size(self):
        while True:
            try:
                width = int(input("Введіть ширину ASCII-арту: "))
                return width
            except ValueError:
                print("Недійсний ввід. Введіть правильну ширину.")

    def choose_characters(self):
        characters = input("Введіть символ для заміни в ASCII-арті (наприклад, @, #, *): ")
        return characters

    def preview_art(self, art, color):
        colored_art = colored(art, color)
        print("Попередній перегляд ASCII-арту:")
        print(colored_art)

    def save_to_file(self, art):
        while True:
            choice = input("Чи бажаєте ви зберегти це у файлі? (так/ні): ").lower()
            if choice == 'так':
                filename = input("Введіть ім'я файлу для збереження ASCII-арту: ")
                with open(filename, 'w') as file:
                    file.write(art)
                break
            elif choice == 'ні':
                break
            else:
                print("Недійсний вибір. Введіть 'так', щоб зберегти або 'ні', щоб не зберігати.")

    def run_generator(self):
        self.get_user_input()
        font = self.select_font()
        color = self.select_color()
        width = self.choose_size()
        characters = self.choose_characters()
        art = pyfiglet.figlet_format(self.text, font=font)
        art = art.encode('utf-8', 'replace').decode('utf-8')
        self.preview_art(art, color)
        self.save_to_file(art)

if __name__ == '__main__':
    while True:
        print("Головне меню:")
        print("1. Створити ASCII-арт")
        print("2. Вийти")
        option = input("Виберіть опцію (1 або 2): ")
        if option == '1':
            generator = ASCIIGenerator()
            generator.run_generator()
        elif option == '2':
            break
        else:
            print("Недійсна опція. Будь ласка, виберіть правильну опцію.")
