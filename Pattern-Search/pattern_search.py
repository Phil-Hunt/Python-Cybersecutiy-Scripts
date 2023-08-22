import re
import os

def find_patterns_in_file(file_path):
    try:
        # Open and read the content of the specified file
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Regular expression patterns to search for

            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            ip_address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            url_pattern = r'\bhttps?://[^\s]+'

            # Add more patterns above as needed
            
            # Search for patterns in the content using regular expressions

            email_matches = re.findall(email_pattern, content, re.IGNORECASE)
            ip_address_matches = re.findall(ip_address_pattern, content)
            url_matches = re.findall(url_pattern, content)

            # Add more searches for other patterns
            
            print("Email addresses found:", email_matches)
            print("IP addresses found:", ip_address_matches)
            print("URLs found:", url_matches)
            # Print more results for other patterns
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def main():
    # Prompt the user to input the path of the file to analyze
    file_path = input("Enter the path to the file to analyze: ")
    find_patterns_in_file(file_path)

if __name__ == "__main__":
    main()
