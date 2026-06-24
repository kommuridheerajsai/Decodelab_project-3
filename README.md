#  Random Password Generator

##  Overview

The Random Password Generator is a Python-based application that creates secure and unpredictable passwords using a combination of letters, digits, and optional special characters. This project demonstrates the use of Python's built-in `random` and `string` modules for generating strong passwords and enhancing account security.

Developed as part of the **DecodeLabs Python Internship Program**, this project focuses on string manipulation, module integration, loops, functions, and input validation.

---

##  Objectives

- Generate random and secure passwords.
- Allow users to specify password length.
- Provide an option to include special characters.
- Generate multiple passwords in a single execution.
- Practice Python libraries and string operations.

---

##  Features

✔ Generate passwords of custom length  
✔ Include uppercase and lowercase letters  
✔ Include numeric digits (0-9)  
✔ Optional special characters (`!@#$%^&*`, etc.)  
✔ Generate multiple passwords simultaneously  
✔ Input validation and error handling  
✔ User-friendly console interface

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| random | Random character selection |
| string | Character set generation |

---

##  Project Structure

```text
Random-Password-Generator/
│
├── password_generator.py
├── README.md
│
└── Output Screenshots (Optional)
```

---

##  Working Principle

### Step 1: Import Modules

The application imports:

```python
import random
import string
```

- `random` is used to randomly select characters.
- `string` provides predefined character sets.

### Step 2: Get User Requirements

The user enters:

- Password length
- Whether special characters should be included
- Number of passwords to generate

### Step 3: Create Character Pool

The program combines:

```python
string.ascii_letters
string.digits
```

If special characters are selected:

```python
string.punctuation
```

is added to the character pool.

### Step 4: Generate Password

The program:

1. Selects random characters.
2. Repeats until the required length is reached.
3. Combines characters into a password string.

### Step 5: Display Passwords

Generated passwords are displayed to the user.

---

##  Algorithm

```text
START

Import random and string modules

Create password generation function

Input password length

Validate input

Ask whether special characters are required

Ask how many passwords to generate

Create character pool

Generate password using random selection

Display generated password(s)

END
```

---

##  Installation & Execution

Run the Program

```bash
python password.py
```


##  Concepts Covered

- Python Functions
- Loops (`for`, `while`)
- Conditional Statements
- Exception Handling
- String Manipulation
- Randomization
- User Input Validation
- Python Standard Libraries

---

## 🎓 Learning Outcomes

Through this project, I learned:

- How to import and use Python modules.
- How to generate random data securely.
- How to perform string manipulation.
- How to validate user input effectively.
- How to structure a Python project professionally.

---

## 🔮 Future Enhancements

- Password Strength Analyzer
- Copy Password to Clipboard
- Save Passwords to File
- GUI Version using Tkinter
- Web Application using Flask
- QR Code-Based Password Sharing

---

## 👨‍💻 Author

**Dheeraj Sai Kommuri**

Python Developer Intern  
DecodeLabs Internship Program

---

## 📄 License

This project is created for educational and learning purposes under the DecodeLabs Python Internship Program.
