# The Object-Oriented Programming (OOP) makes the maintainability of your code easier for you, for you in 6 months, and for the developers who will contribute to your library.

# BUT the main reason to write OOP is that when you develop a library, you need to think about: What is the architecture that will make my library as easy to use as possible?
# How do you use a library? You usually import it, instantiate an object and call a method on it. Thus, try to make your library easy to use and Pythonic. Imagine things from the point of view of the user, and you will write code in a clearer and more maintainable way.

# Import Multiplication from your library
# from complex_multiply.multiplication import Multiplication
from complex_multiply import Multiplication
    
# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))

        