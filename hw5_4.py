#Task 4

def input_error(func): # Decorator to handle input errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Not enough parameters."
        except IndexError:
            return "Not enough parameters."
        except KeyError:
            return "Contact not found."
    return inner

def parse_input(user_input): # Function to parse user input
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # Function to add a contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # Function to change a contact's phone number
    name, new_phone = args
    if name in contacts: # Check if the contact exists
        contacts[name] = new_phone
        return "Contact changed."
    else:
        return "Contact not found."
    
@input_error
def phone_number(args, contacts):  # Function to get a contact's phone number
    if args[0] in contacts: # Check if the contact exists
        return contacts[args[0]]
    else:
        return "Contact not found."

def print_all(contacts): # Function to print all contacts
    if len(contacts) == 0: # Check if there are any contacts
        return "No contacts found."
    else:
        result = "Contacts: \n"
        for name, phone in contacts.items(): # Print all contacts
            result += f"{name}: {phone}\n"
        return result
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]: # Exit the program
            print("Good bye!")
            break
        elif command == "hello": # Greet the user
            print("How can I help you?")
        elif command == "add": # Add a contact
            print(add_contact(args, contacts))
        elif command == "change": # Change a contact
            print(change_contact(args, contacts))
        elif command == "phone": # Print the phone number of a contact
            print(phone_number(args, contacts))
        elif command == "all": # Print all contacts
            print(print_all(contacts))  
        else: # Invalid command
            print("Invalid command.")

if __name__ == "__main__":
    main()
