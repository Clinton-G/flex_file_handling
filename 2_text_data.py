import re

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, contents)
            unique_emails = list(set(emails))
            return unique_emails

    except FileNotFoundError:
        print(filename, 'Does Not Exist')


def main():
    filename = 'contacts.txt'
    extracted_emails = extract_emails(filename)
    
    if extracted_emails:
        print("\nUnique Email's:")
        for email in extracted_emails:
            print(email)
    else:
        print("No Email Addresses Found.")

if __name__ == "__main__":
    main()
