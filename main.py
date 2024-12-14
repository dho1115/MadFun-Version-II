if __name__ == "__main__":
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
