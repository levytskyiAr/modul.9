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
def add(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

@input_error
def change(params):
    name, phone = params.split()
    contacts[name] = phone
    return f"Phone number for {name} changed to {phone}"

@input_error
def phone(name):
    return f"The phone number for {name} is {contacts[name]}"

@input_error
def show_all():
    if not contacts:
        return "No contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def process_command(user_input):
    if user_input == "hello":
        return hello()
    elif user_input.startswith("add"):
        return add(user_input.split(maxsplit=1)[1])
    elif user_input.startswith("change"):
        return change(user_input.split(maxsplit=1)[1])
    elif user_input.startswith("phone"):
        return phone(user_input.split(maxsplit=1)[1])
    elif user_input == "show all":
        return show_all()
    else:
        return "Invalid command. Type 'help' for a list of commands."

def main():
    while True:
        user_input = input("Enter command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            result = process_command(user_input)
            print(result)

if __name__ == "__main__":
    main()
