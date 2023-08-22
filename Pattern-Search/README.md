# Regular Expression Pattern Finder

This is a simple Python program that allows a cyber security analyst or anyone wanting to filter large amounts of data to find specific regular expression patterns in a given text file. The program uses the `re` library to search for patterns such as email addresses, IP addresses, and URLs within the file content.

## How to Use

1. Clone this repository to your local machine or download the `pattern_finder.py` script.

2. Make sure you have Python installed on your machine. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

3. Open a terminal or command prompt and navigate to the directory where you have saved the `pattern_finder.py` script.

4. Run the program by entering the following command: python pattern_finder.py ### (FYI if 'python pattern_finder.py' doesnt work try 'python3 pattern_finder.py')

5. The program will prompt you to enter the path to the file you want to analyze. Provide the full path, including the file name and extension (e.g., C:\Documents\sample.txt).

6. The program will then search for various patterns in the file content using regular expressions. The patterns currently supported include:
    Email addresses
    IP addresses
    URLs

You can easily customize the patterns by modifying the regular expressions defined in the find_patterns_in_file function of the script.

After analyzing the file, the program will display the results for each pattern it found in the file.

## Customizing Patterns

If you want to search for additional patterns or modify the existing ones, you can do so by editing the pattern_finder.py script. In the find_patterns_in_file function, you'll find a section where the regular expression patterns are defined. You can add, remove, or modify patterns as needed.

## Example Usage

Suppose you have a file named sample.txt with the following content:


Contact us at support@example.com or visit https://www.example.com
IP addresses: 192.168.1.1, 10.0.0.1

When you run the program and provide the path to sample.txt, you will get output similar to the following:

### Enter the path to the file to analyze: sample.txt


Email addresses found: ['support@example.com']
IP addresses found: ['192.168.1.1', '10.0.0.1']
URLs found: ['https://www.example.com']


Contributions to this project are welcome! If you have ideas for improvements or additional features, feel free to fork this repository and submit a pull request!



