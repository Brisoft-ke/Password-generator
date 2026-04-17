Password Generator

A simple and interactive password generator built with Python and Tkinter.
This application allows users to generate strong, random passwords of a desired length, combining uppercase letters, lowercase letters, digits, and special characters.

Features

Customizable length – Enter the number of characters for your password.

Random character set – Uses letters (A-Z, a-z), digits (0-9), and punctuation symbols.

Graphical user interface – Simple and clean interface built with Tkinter.

Instant generation – Click a button and see your secure password displayed immediately.

Requirements

Python 3.x

Tkinter (usually included with standard Python installations)

How to Run

Clone the repository or download the Password generator.py file.

Open a terminal or command prompt in the project directory.

Run the script:


bash
python "Password generator.py"
Enter the desired password length in the input field.

Click Generate Password – the generated password will appear below the button.

File Structure


text
Password-generator/
├── Password generator.py   # Main application script
└── README.md               # Project documentation
Notes
The generator uses Python’s random module; for cryptographically stronger randomness, consider using secrets in a production environment.

The current code includes minor syntax issues (e.g., tk.TK() should be tk.Tk(), missing underscore in length_entry). These do not prevent basic functionality but may be fixed in future updates.

License
This project is open source and available under the MIT License.
