#  METHOD USED
#  Kramer Kilroy
#  CSCI 102 – Section A
#  Week 12 - Part A

PrintOutput is a fairly simple function. All that was required was to write the function to take and argument and then print that same statment with 'OUTPUT' before it.

LoadFile uses the built in functions in python to open and read a file. To get a list as output I ued the .split command to split the file at the new line symbol (\n). I used this because the built in function of readlines returned a list of each line including the new line character.

UpdateString is a bit more challenging because we are asked to modify a string, something python does not allow directly. I used a string slice method to make a new string that is the original cut at the given index and insering the replacement character. To close the slice I 'reattached' the string one index past the chosen index so it excludes that character, effectivly replacing it with the new one.

FindWordCount I initialized the variable 'count' to zero. A for loop was used to pass through all the characters in the list. The loop checked each character in the list to see if it matched the given string. If it did the variable was incimented by posotive one. After the loop concludes the value of the count variable is printed.

ScoreFinder uses a more complicated method. The complexity comes from making the function work for upper and lower case words. The input string is lowered, then the list a is lowered character by caracter in a for loop. Then it is joined in a string with the .join operation. To check if the name is in the list I used the .find() function and if it returned negative one it would give the player not found output. Each character of the lowered list was checked against the lowered string, if it was found the index was used for the print statment.

Union was simply using the addition operator to join the two lists.

Intersection I initialized a new list and appeneded the characters that were in both lists to this new list using a for loop. Then returned the list of common charicters

NotIn follows the same method as Intersection but instead of making a list of common charicters it made a list of characters from the first list that did not appear in the second list.
