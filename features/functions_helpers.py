extractFunctions = lambda iter: {key:value for key, value in iter if "__" not in key}; # The if "__" not in key is to remove all extraneous, non-math functions (that start and end with "__").
