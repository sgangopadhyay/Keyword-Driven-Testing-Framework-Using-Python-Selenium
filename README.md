# Keyword Driven Testing Framework Using Python Selenium

## Overview
This project implements a **Keyword Driven Testing Framework** using Python and Selenium. It allows you to define test cases in a YAML file and execute them using a Selenium-based automation script. The framework is designed to be modular, easy to use, and extendable.

---

## Functionality
The framework performs the following tasks:
1. Reads test cases from a YAML file.
2. Executes the test steps defined in the YAML file using Selenium.
3. Validates the functionality of the SauceDemo website, including:
   - Login functionality.
   - Visibility of input fields and buttons.
   - Navigation to the dashboard after successful login.
4. Provides detailed logs of test execution.

---

## Programmer
- **Name**: Suman Gangopadhyay
- **Email**: [linuxgurusuman@gmail.com](mailto:linuxgurusuman@gmail.com)

---

## Project Details
- **Date**: 1-Jan-2025
- **Version**: 1.0
- **Code Library**: Selenium
- **Prerequisites**:
  - Python 3.x
  - Selenium
  - ChromeDriver
  - PyYAML (for parsing YAML files)

---

## Installation and Setup

### Step 1: Install Python
Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

### Step 2: Install Required Libraries
Install the required Python libraries using pip:
```bash
pip install selenium pyyaml webdriver-manager
```

### Step 3: Download ChromeDriver
Ensure ChromeDriver is installed and matches your Chrome browser version. You can download it from ChromeDriver.

### Project Structure
```bash
project/
│
├── SauceDemoMain.py          # Main automation script
├── test_case.yaml            # YAML file containing test cases
├── KeywordDrivenFramework.py # Framework to execute test cases
└── README.md                 # Project documentation
```

### How to Run the Framework
  1. Clone the repository or download the project files.

  2. Navigate to the project directory:
     ```bash
     cd project
     ```
  4. Run the framework:
     ```bash
     python test_runner.py
     ```
### Example YAML File (test_case.yaml)
```yaml
test_cases:
  - name: "Validate Login Functionality"
    steps:
      - action: "start"
      - action: "validate_username_input_box"
      - action: "validate_password_input_box"
      - action: "validate_submit_button"
      - action: "validate_login"
      - action: "shutdown"
```

### License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
