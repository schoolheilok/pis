/*
## Question 1: Statements and Expressions (10 points)  
- Write three lines of Python code that include:  
  - An assignment statement assigning a value to a variable  
  - A print statement displaying a message  
  - An expression involving arithmetic operations  
- Add comments explaining which line is a statement and which is an expression.
*/

temperature = 25 # Assignment statement  
today = temperature + 10  # temperature + 10 is an expression that evaluates to 35 if x is 25
print("Hi welcome, today's temperature is ",today,"degrees celsius")

## Question 2: Variables and Assignments (10 points)  
- Create variables to store your name (string), age (integer), and height in meters (float).  
- Print a sentence that uses all three variables, ensuring age and height are converted to strings for concatenation if needed.

name = "James" # String
age = 19 # Integer
height = 1.82 # Float
print("I am",name,", and I am",age,"years old,", "and I am",height,"tall.")

---

## Question 3: Data Types and Type Conversion (10 points)  
- Write code to take a string variable with a number (e.g., `"25"`), convert it to an integer, then to a float, and print all three values with labels.  
- Add comments explaining the conversions.

number = "2" # String
print(number)
print(int(number)+5) # Changed to Integer by adding int() to add another number 
print(float(number)+5) # Changed to float by adding float() 

---

## Question 4: Input and Output (10 points)  
- Write a Python program that prompts the user to input their favorite color and then prints a message including that color.

x = input("Your favorite color: ")
print("My favorite color is",x)
---

## Question 5: Naming Conventions and Principles (10 points)  
- Identify and correct the errors in the following variable names:  
  - `1stPrize`  
  - `user Email`  
  - `CalculateTotal` (explain if this is good or bad in Python variable context)  
- Briefly explain why good naming helps with the **KISS** and **DRY** programming principles.

`1stPrize`  # numbers and letters are together
`user Email`  # there's a space between letters
`CalculateTotal` # lack of snake_case for variables and functions
 **KISS** emphasizes that solutions should be simple and **DRY** avoids repeating code
---

## Question 6: Working with Lists (10 points)  
- Create a list containing three programming languages you want to learn.  
- Assign that list to a variable and print the list.

x = ["python, java, C+"]
print(x)
---

## Question 7: Working with Tuples (10 points)  
- Create a tuple with three numbers.  
- Write a comment that explains what happens if you try to change a value in this tuple.


---

## Question 8: Boolean Data Type (10 points)  
- Create three variables:  
  - One assigned `True`  
  - One assigned `False`  
  - One assigned the result of the expression `5 > 3`  
- Print the value of all three variables with labels.

---

## Question 9: String Manipulation (10 points)  
- Create a variable with your full name as a string.  
- Print the string in all uppercase letters and then in lowercase letters [name.upper(), name.lower()].

---

## Question 10: Early Debugging (10 points)  
- Write a Python snippet that assigns a number to a variable and prints double its value.  
- Intentionally insert a syntax error (such as a missing parenthesis) and describe how you would detect and fix the error.

---
