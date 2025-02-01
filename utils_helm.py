"""
Module: utils_helm

Purpose: Reusable Module for My Analytics Projects 

Description: This module provides information about Treefort Drop In Hourly ChildCare and highlights important information for parents in search of quality childcare in the Omaha area.
Author: Diamond Helm

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_childcare_for_ages_newborn_to_school_ age: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
number_of_staff_memebers: int = 15

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
parent_satisfaction: float = 4.9

# declare a list of strings
# TODO: Add or replace this with your own list  
classrooms_offered: list = ["Infants", "Toddler", "Transitional PreK", "Preschool and School Age" ]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
children_per_day: list = [4, 10, 14, 19]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_children: float = min(children_per_day)  
max_children: float = max(children_per_day)  
mean_children: float = statistics.mean(children_per_day)  
stdev_children: float = statistics.stdev(children_per_day)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
--------------------------------------------------------
Treefort Drop In Hourly Child Care Facts
--------------------------------------------------------
Has Childcare for infans to school age:  {has_infant_to_school_age}
Number of staff members:         {number_of_staff_members}
Classrooms Offered:             {Classrooms_offered}
Parent Satisfaction Scores: {client_satisfaction_scores}
Minimum Children Per Day: {min_Children_per_day}
Maximum Children Per Day: {max_Children_per_day}
Mean Children Per Day: {mean_Children_per_day:.2f}
Standard Deviation of Satisfaction Scores: {stdev_Children_per_day:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
