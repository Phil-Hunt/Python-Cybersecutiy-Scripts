import re

log_file = 'example.txt'  # Replace 'example.txt' with the actual path of the log file you want to work with.
pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # The pattern variable contains the regular expression pattern used to search for IP addresses in the log file. The provided pattern r'\b(?:\d{1,3}\.){3}\d{1,3}\b' is designed to match IPv4 addresses.

try:
      # Open and read the log file
    with open(log_file, 'r') as file:
        # Read the contents of the log file
        log_contents = file.read()
        # Search for IP addresses using the specified pattern
        found_entries = re.findall(pattern, log_contents)
        
        
         # Check if any matching entries were found
        if found_entries:
            print("Found matching entries:")
       
            # Iterate through the found IP addresses and print them
            for entry in found_entries:
                print(entry)
        else:
            print("No matching entries found.")


       # Handle the case when the log file is not found     
except FileNotFoundError:
    print(f"Error: Log file '{log_file}' not found.")
