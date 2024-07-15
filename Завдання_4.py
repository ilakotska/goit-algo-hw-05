def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments."
    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args, contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def unknown_command(args, contacts):
    return "Unknown command"

COMMANDS = {
    "add": add_contact,
    "phone": get_phone,
    "all": show_all
}

def parse_command(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def main():
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["exit", "close", "goodbye"]:
            print("Goodbye!")
            break
        command, args = parse_command(user_input)
        handler = COMMANDS.get(command, unknown_command)
        result = handler(args, contacts)
        print(result)

if __name__ == "__main__":
    main()
