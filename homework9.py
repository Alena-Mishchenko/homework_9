
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, TypeError):
            return "Enter a valid command."
    return wrapper

contacts = {}


@input_error
def hello(): 
    return "How can I help you?"


@input_error
def goodbye():
    return "Good bye!"


@input_error
def add(args):
    parts = args.split()
    if len(parts) == 2:
        name, phone = parts
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) == 12 or len(phone) == 10:
            contacts[name] = phone
            return f"Added {name} with phone {phone}."
        else:
            return "Phone number must be 10 or 12 digits."
    else:
        return "Invalid format. Please enter name and phone number."

@input_error
def show_all(): 
    result = ""
    if contacts:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        result = "No contacts found."
    return result

@input_error
def phone(args):
    name = args
    if name in contacts:
        return contacts[name]
    else:
        return f"{name} not found in contacts."
   
@input_error
def change(args):
    name, new_phone = args.split()
    if name in contacts:
        contacts[name] = new_phone
        return f"Changed phone for {name} to {new_phone}."
    else:
        return f"{name} not found in contacts."

@input_error  
def no_command(): 
    return "Unknow command"

handler = {
    "add": add,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "hello": hello
}

def parser(text: str)-> tuple[callable,str]:
    words = text.split()
    command = words[0]
    if command in handler:
        args = ' '.join(words[1:])
        return handler[command], args 
    return no_command, None


def main():
    print("Hello. Bot is ready.Enter 'hello' for assistance.")
    while True:
        user_input = input("Enter a command or 'bye' to quit: ").lower()
        if user_input in ["good bye","bye","close", "exit", "quit"]:
            print(goodbye())
            break
        command, data = parser(user_input)
        if data:
            result = command(data)
        else:
            result = command()    
        print(result)


if __name__ =="__main__":
    main()