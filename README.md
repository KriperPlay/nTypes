# nTypes

# Description

// !!!I WRITE THIS LIB FOR FUN, DONT USE THIS FOR SERIOS PROJECTS!!!
// This documentation wriren by chat-gpt4o
// I wrote the project myself

The nVar project is a class for handling variables of various types, including strings, integers, floating-point numbers, arrays, and boolean values. All data is stored as hexadecimal strings to ensure security and consistency.

# Installation

Just import lib into u project

# Classes

# nVar

The main class for working with variables. It provides methods for creating and processing variables of different types.

# Attributes

• types: A dictionary where keys are variable names and values are tuples containing the variable type and its value as a hexadecimal string.

• numbersf: A list of string representations of digits from 0 to 9.

# Methods

• __init__(self): Constructor of the class, initializes the types and numbersf attributes.

• create_var(self, var: str, _type: str, filling): Creates a new variable with a given name, type, and value.

  • var: The name of the variable.

  • _type: The type of the variable (can be "nstr", "nint", "nfloat", "narray", "nbool").

  • filling: The value to be assigned to the variable.
  
  Exceptions:

  • ValueError: If the value does not match the expected type.

  • TypeError: If the variable type does not match the expected one.

• nvar_var(self, var: str) -> (int | str | float | bool | list): Returns the value of the variable by its name in its original format.

  • var: The name of the variable.

• isinstance(self, var: str, _type: str) -> bool: Checks whether the variable of a given name is of the specified type.

  • var: The name of the variable.

  • _type: The expected type of the variable.

# Usage Examples

```python
#Import lib
from ntypes import nVar

# Create an instance of the nVar class
my_vars = nVar()

# Create a string variable
my_vars.create_var("my_string", "nstr", "Hello World")

# Create an integer variable
my_vars.create_var("my_int", "nint", 123)

# Create a floating-point variable
my_vars.create_var("my_float", "nfloat", 123.456)

# Create an array
my_vars.create_var("my_array", "narray", [1, 2, 3])

# Create a boolean variable
my_vars.create_var("my_bool", "nbool", "real")

# Retrieve variable values
print(my_vars.nvar_var("my_string"))  # Hello World
print(my_vars.nvar_var("my_int"))     # 123
print(my_vars.nvar_var("my_float"))   # 123.456
print(my_vars.nvar_var("my_array"))    # [1, 2, 3]
print(my_vars.nvar_var("my_bool"))    # True

# Check variable type
print(my_vars.isinstance("my_int", "nint"))  # True
```
# End
thx for checked ntypes <3
