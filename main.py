def read_contacts(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        contacts = file.readlines()
    return contacts

def sort_contacts(contacts):
    return sorted(contacts, key=lambda x: x.lower())

def write_contacts(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(contact)

def main():
    contacts = read_contacts('contacts.txt')
    sorted_contacts = sort_contacts(contacts)
    write_contacts('contacts_sorted.txt', sorted_contacts)

if __name__ == '__main__':
    main()
