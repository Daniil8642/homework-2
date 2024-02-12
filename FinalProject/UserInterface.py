#UserInterface.py
from abc import ABC, abstractmethod
from Bot import Name, Phone , Birthday , Email , Status , Note , Record , AddressBook

class UserInterface(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def get_user_input(self, prompt):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass

class ConsoleUserInterface(UserInterface):
    def display_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return input(prompt)

    def display_contacts(self, contacts):
        for contact in contacts:
            print(contact)

# Modify the Bot class to accept a UserInterface
class Bot:
    def __init__(self, user_interface):
        self.book = AddressBook()
        self.user_interface = user_interface

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)

        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)

        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)


        elif action == 'view':
            self.user_interface.display_contacts(self.book)

        elif action == 'exit':
            self.user_interface.display_message("Exiting the contact assistant. Goodbye!")
            # Add any necessary cleanup or finalization code here
            exit()

        else:
            self.user_interface.display_message("There is no such command!")


if __name__ == "__main__":
    console_interface = ConsoleUserInterface()
    bot = Bot(console_interface)

    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    
    while True:
        action = console_interface.get_user_input('Type help for a list of commands or enter your command\n').strip().lower()

        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                print(format_str.format(command))
            action = console_interface.get_user_input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
#UserInterface.py
        