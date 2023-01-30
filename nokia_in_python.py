from nokia_in_python_functionalities import *
def menu_prompt():
    option =eval(input("""Welcome to menu  
    1 --> phone book 
    2 --> messages 
    3 --> call register  
    4 --> chat """))
    return option

def  menu(option):
    match(option):
        case 1:
            phone_book(phone_book_prompt())
        case 2:
            messages(message_prompt())
        case 3:
            # call_register()
            print("call register")
        case 4:
            # chat()
            print("chat")

def phone_book_prompt():
     option = eval(input("""
     Welcome to phone book
     1--> search
     2--> save contact
     3--> display all contacts
     4--> delete contact
     5--> menu
     """))
     return option

def phone_book(option):
    match(option):
        case 1:
            print("search")
            search_contacts(input("Enter contact name "))
            inner_option(inner_option_prompt())            
        case 2:
            print("save contact")
            save_contact_function()
            inner_option(inner_option_prompt())
        case 3: 
            print("Display all")
            display_all_contact()
            inner_option(inner_option_prompt())
        case 4:
            print("delete contact")
            inner_option(inner_option_prompt())
        case 5:
            menu(menu_prompt())

def message_prompt():
    option = eval(input("""
    Welcome to messages
    1--> write message
    2--> inbox
    3--> outbox
    4--> draft
    5--> menu
    """)) 
    return option

def messages(option):
    match (option):
        case 1:
            print("write message")
            inner_option(inner_option_prompt())
        case 2:
            print ("inbox")
            inner_option(inner_option_prompt())
        case 3:
           print("outbox")
           inner_option(inner_option_prompt())
        case 4: 
            print("drarft")
            inner_option(inner_option_prompt())
        case 5:
            menu(menu_prompt())

def inner_option_prompt():
    option = eval(input("""
    1--> back to menu
    """)) 
    return option
def inner_option(option):
    if option == 1:
        menu(menu_prompt())

# def save_contact_function():
#     phone_numbers ={}
#     phone_numbers = input("Enter the name ")
#     phone_numbers =input("Enter the number ")
#     print(phone_numbers)
    


menu(menu_prompt())