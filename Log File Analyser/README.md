## Log Analysis Python Script

# The is a simple Python script that allows a cybersecurity analyst or anyone needing to search log files to look for specific strings or patterns. Simply import a log file and search for specific patterns using regular expressions.
# If matching entries are found, they will be displayed in the terminal. If no matching entries are found, a message indicating that will be displayed.


## Prerequisites

Before using this program, make sure you have Python installed on your system. You can download Python from the official website: [Python Download](https://www.python.org/downloads/)


## Usage

1. Place the log file you want to analyze in the same directory as the script or provide the full path to the log file in the `log_file` variable.

2. Open the terminal or command prompt.

3. Navigate to the directory containing the script and the log file.

4. Run the program using the following command: python log_file_analyser.py


## Configuration

You can customize the program by modifying the following variables in the script:

1. log_file: Provide the path to the log file you want to analyse.
1. pattern: Modify the regular expression pattern to match the specific string pattern you're searching for in the log file. The example pattern provided matches IP addresses.

# Example Scenario

Suppose you have a log file named sample.txt containing various IP addresses. You want to find and display all the IP addresses in the log file. You can follow the steps mentioned above to run the program and obtain the results.

Feel free to modify and extend this program to suit your needs. If you encounter any issues or have suggestions for improvement, please feel free to contribute
