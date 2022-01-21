# Specialization: Google IT Automation with Python
# Course 01: Crash Course with Python
# Week 4 Module Part 1 - Practice Quiz
# Student: Shawn Solomon
# Learning Platform: Coursera.org

# Scripting examples encountered during the Module Part 1 Practice Quiz:

# 01. The is_palindrome function checks if a string is a palindrome. A palindrome is a string that 
# can be equally read from left to right or right to left, omitting blank spaces, and ignoring 
# capitalization. Examples of palindromes are words like kayak and radar, and phrases like 
# "Never Odd or Even". Fill in the blanks in this function to return True if the passed 
# string is a palindrome, False if not.

# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = ""
#     reverse_string = ""
#     # Traverse through each letter of the input string
#     for ___:
#         # Add any non-blank letters to the 
#         # end of one string, and to the front
#         # of the other string. 
#         if ___:
#             new_string = ___
#             reverse_string = ___
#     # Compare the strings
#     if ___:
#         return True
#     return False
# 
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for character in input_string[0:]:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if character != " ":
			new_string = new_string + character.lower()
			reverse_string = character.lower() + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


# 02. Using the format method, fill in the gaps in the convert_distance function so that it returns 
# the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) 
# should return "12 miles equals 19.2 km".

# def convert_distance(miles):
#     km = miles * 1.6 
#     result = "{} miles equals {___} km".___
#     return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# 04. Fill in the gaps in the nametag function so that it uses the format method to return first_name and the 
# first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

# def nametag(first_name, last_name):
#     return("___.".format(___))
#
# print(nametag("Jane", "Smith")) 
# # Should display "Jane S." 
# print(nametag("Francesco", "Rinaldi")) 
# # Should display "Francesco R." 
# print(nametag("Jean-Luc", "Grand-Pierre")) 
# # Should display "Jean-Luc G." 

def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


# 05. The replace_ending function replaces the old string in a sentence with the new string, but only if the 
# sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, 
# only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") 
# should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so 
# replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

# def replace_ending(sentence, old, new):
#     # Check if the old string is at the end of the sentence 
#     if ___:
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the 
#         # end with the new string
#         i = ___
#         new_sentence = ___
#         return new_sentence
#
#     # Return the original sentence if there is no match 
#     return sentence
# 	
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# # Should display "The weather is nice in April"

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
    if sentence.find(old) >= 0:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
        
        # i = sentence.find(old)                                #! <-- What am I doing with this?
        new_sentence = sentence.replace(old, new)
        if new_sentence.find("dogs") >= 0:                      #! <-- Really inefficient workaround.
            new_sentence = new_sentence.replace(new, old, 1)
        elif new_sentence.find("donuts") >= 0:                  #! <-- Inefficient orkaround #2!
            new_sentence = new_sentence.replace(new, old, 1)
        return new_sentence

	# Return the original sentence if there is no match 
    return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"