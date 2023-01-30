contacts = []
def save_contact():
    
    contacts.append(input("Enter the contact name "))
    contacts.append(input("Enter the contact number "))

def search_contacts(contact_name):
    for i in range (len(contacts)):
        if contact_name == contacts[i]:
            print("The name is ", contacts[i])
            print("The number is ", contacts[i+1])