
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Incorrect input. Enter the contact name please"
        except ValueError:
            return "Incorrect input. Please input in this format >>> add [name] [phone]"
        except IndexError:
            return "Data are missing. Make sure you entered contact before."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact is added"

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return f"Name {name} is not in your contacts. Add the new contact."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"{name} is not in your contacts"

@input_error    
def show_all(contacts):
   if not contacts:
    return "No contacts saved yet"
   else:
    result = "Your contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command >>> ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
                print(add_contact(args, contacts))
        elif command == "change":
                print(change_contact(args, contacts))
        elif command == "phone":
                print(show_phone(args, contacts))
        elif command =="all":
                print(show_all(contacts))
        else:
            print("Unkwnown command. Try again, please.")

if __name__ == "__main__":
    main()