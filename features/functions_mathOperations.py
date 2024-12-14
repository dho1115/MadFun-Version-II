'''
\t*** Add any new math functions inside THIS file!!! ***\n\n
Also, I did NOT import math as a global variable because I do NOT want it to show up as one of the properties when I print(MathOperationsDictionary = features.functions_mathOperations.__dict__.items()) in main.py.\n
Rather, I imported math inside the BODY of the squareRoot function.
'''

def roundNumber (num, decimalPlaces=0): #If your function takes in MORE than 1 parameter, follow this template.
   try:
      roundToZero = input(f"Is it okay if I round {num} to zero decimal places (y/n)? ");
      if roundToZero == 'n': #User wants to round to another number other than zero.
         howManyPlaces = input("Fine. How many places do you want me to round to? ");
         try:
            decimalPlaces = int(howManyPlaces);
            return round(num, decimalPlaces);
         except Exception:
            print(Exception);
            return f"Sorry, I cannot round to {howManyPlaces} because it is not an integer.";
   except Exception:
      print(Exception)
      return "Sorry... an exception occured somewhere"
   return round(num, decimalPlaces);

absoluteValue = lambda num: abs(num);
def squareRoot(num):
   from math import sqrt; #I scoped this to the function because I do not want this to show up as one of the properties when I run extractFunctions(dictionary).
   return sqrt(absoluteValue(round(num)));

