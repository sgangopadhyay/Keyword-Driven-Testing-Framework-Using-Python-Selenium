# test_runner.py

"""
Description : Keyword Driven Testing Framework (KDTF) Test Runner file 
Programmer : Suman Gangopadhyay
Email ID : linuxgurusuman@gmail.com
Date : 24-Feb-2025
Version : 1.0
Code Library : Selenium
Prerequisites : Python, Selenium, ChromeDriver, YAML
"""

# Import necessary modules
import yaml  # For parsing YAML files
from SauceDemoMain import SauceDemoAutomation  # Import the automation class
from SauceDemoMain import Data  # Import the data class containing URLs and credentials


class KeywordDrivenFramework:
    """
    This class implements a Keyword Driven Testing Framework.
    It reads test cases from a YAML file and executes them using the SauceDemoAutomation class.
    """

    def __init__(self, yaml_file):
        """
        Constructor to initialize the framework.
        :param yaml_file: Path to the YAML file containing test cases.
        """
        self.yaml_file = yaml_file  # Store the path to the YAML file
        self.automation = SauceDemoAutomation(Data().URL)  # Initialize the automation class with the application URL

    def load_test_cases(self):
        """
        Load test cases from the YAML file.
        :return: A dictionary containing the test cases.
        """
        with open(self.yaml_file, 'r') as file:
            return yaml.safe_load(file)  # Parse and return the YAML file content

    def execute_test_case(self, test_case):
        """
        Execute a single test case by running its steps.
        :param test_case: A dictionary containing the test case name and steps.
        """
        print(f"Executing Test Case: {test_case['name']}")  # Print the test case name
        for step in test_case['steps']:  # Iterate through each step in the test case
            action = step['action']  # Get the action (method name) from the step
            if hasattr(self.automation, action):  # Check if the action exists in the automation class
                method = getattr(self.automation, action)  # Get the method corresponding to the action
                result = method()  # Execute the method
                print(f"Action: {action}, Result: {result}")  # Print the action and its result
            else:
                print(f"Action: {action} not found in SauceDemoAutomation class")  # Print error if action is not found

    def run(self):
        """
        Run all test cases loaded from the YAML file.
        """
        test_cases = self.load_test_cases()  # Load test cases from the YAML file
        for test_case in test_cases['test_cases']:  # Iterate through each test case
            self.execute_test_case(test_case)  # Execute the test case


# Entry point of the script
if __name__ == "__main__":
    # Initialize the framework with the path to the YAML file
    framework = KeywordDrivenFramework("test_case.yaml")

    # Run the framework to execute all test cases
    framework.run()
