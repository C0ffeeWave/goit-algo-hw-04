def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Невірна команда. Формат: add [ім'я] [телефон]")
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."
    except Exception as e:
        return str(e)

def change_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Невірна команда. Формат: change [ім'я] [телефон]")
        name, phone = args
        if name not in contacts:
            raise ValueError("Контакт не знайдено.")
        contacts[name] = phone
        return "Контакт оновлено."
    except Exception as e:
        return str(e)

def show_phone(args, contacts):
    try:
        if len(args) != 1:
            raise ValueError("Невірна команда. Формат: phone [ім'я]")
        name = args[0]
        if name not in contacts:
            raise ValueError("Контакт не знайдено.")
        return contacts[name]
    except Exception as e:
        return str(e)

def show_all(contacts):
    if not contacts:
        return "Контакти не знайдено."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
