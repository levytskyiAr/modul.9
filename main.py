def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Type 'help' for a list of commands."
    return wrapper

contacts = {}

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

@input_error
def change_contact(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Phone number for {name} changed to {phone}"

@input_error
def phone_contact(name):
    return f"The phone number for {name} is {contacts[name]}"

@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    while True:
        command = input("Enter command: ").lower()

        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command.startswith("add"):
            params = input("Enter name and phone (separated by space): ")
            print(add_contact(params))
        elif command.startswith("change"):
            params = input("Enter name and new phone (separated by space): ")
            print(change_contact(params))
        elif command.startswith("phone"):
            name = input("Enter name: ")
            print(phone_contact(name))
        elif command == "show all":
            print(show_all_contacts())
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()

