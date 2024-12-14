if __name__ == "__main__":
   '''
   This program will: (1) round the number, (2)calculate the square root and (3) calculate the absolute value of the number inputted.

   Do you want to add another operation? Just go to function_mathOperations.py and add a new function that takes in 1 parameter (the number).

   IF your function takes in more than one paramter, please follow the directions for the roundNumber function!!!
   '''
   import features.functions_mathOperations;
   from features.functions_helpers import extractFunctions;

   dictionary = features.functions_mathOperations.__dict__.items();
   MathOperationsDictionary = extractFunctions(dictionary);

   number = input("Please input a number: ")
   try:
      number = float(number)
      for key, value in MathOperationsDictionary.items():
         print(f"The {key} of {number} is {extractFunctions(dictionary)[key](number)}.");
   except Exception:
      print(f"Sorry... {number} must be a number!!!")
