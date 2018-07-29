##############################
# Name : Class_08_Outline.py #
# Author : Tyler Pierce      #
# Desc: Outline for Class_08 #
##############################

# This class we will be going over some more
# rudimentary things that we have skipped 
# over in the previous lessons.

# We shall cover variables, values and types

# Enter into the interpreter (From here on 
# three chevrons ">>>" denotes the python 
# interpreter) :

# >>> score = 0

# Now if we want to see the value stored in the
# variable "score" we can use print : 

# >>> print(score)

# Note that if we print something that does not
# exist that python will give an error :

# >>> print(myvariable)

# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'myvariable' is not defined

# Python gives us a nice warning that says the 
# variable we just tried to print is undefined

# Now let's change the value

# >>> score = 1

# If we print score again we see that 1 is the 
# value returned

# >>> print(score)

# Now let's add one to score

# >>> score = score + 1

# Printing the value of scrore shows 2 now

# >>> print(score)

# In python we follow this naming convention
# when naming variables:

# >>> high_score = 1000

# In this way the variable is defined as 
# being lowercase and with an underscore 
# between names as well as being descriptive


# In these examples we have been using numbers
# however that doesn't have to be the case

# >>> player_name = "Ben"

# We can even switch a name between numbers and
# text

# >>> our_variable = 1000
# >>> print(our_variable)
# >>> our_variable = "Some Text"
# >>> print(our_variable)

# Now that we've come accross number and this other
# type. We need to learn about types of values

# >>> type(3)

# This seems to be of type int. This stands for 
# integer (whole number)

# >>> type("3")

# Did you catch that? The value type returned is not
# int but rather a str which stands for string

# Python interprets something nested in quotation
# marks differently than something not nested in
# those quotation marks. To see what we mean type : 

# >>> 3+3

# >>> "3" + "3"

# The first will add the two numbers together where 
# the second will join the pieces of text together

# >>> type(3.0)

# >>> type(3>2)

# or 

# >>> type(True)


# Storing Numbers

# The type of a particular piece of data affects what
# python can do with it. Let's first start with the 
# numeric types int and float

# While there are many different operations we can do
# with numbers there are only two types of operations
# we can do. comparisons and numerical operations
print("")
print("Comparison or Logical Operators")
print('######################################################################################')
print("Operator:		Meaning:			Example:")
print("<			less than			3<2 is false")
print("> 			greater than 			3>2 is true")
print("== 			equal to 			3==3 is true")
print("<=			less than or equal to 		3<=2 is false")
print(">=			greater than or equal to 	3>=2 is true")
print("!=			not equal to 			3!=4 is true")
print('######################################################################################')
print("")


print("Numerical Operators")
print('######################################################################################')
print("Operator:		Meaning:			Example:")
print("+			addition			2+2 is 4")
print("- 			subtraction 			3-2 is 1")
print("* 			multiplication 			2*3 is 6")
print("/			division 			10/2 is 5")
print("%			divide and take remainder 	5%2 is 1")
print("**			to the power 			4**2 is 16")
print("int()			convert to integer 		int(3.2) is 3")
print("float()			convert to float 		float(2) is 2.0")
print('######################################################################################')
print("")

# Now that is the operations of numbers so we shall 
# move on to strings

# Strings

# Strings can be created by enclosing something in
# quotation marks. Either single or double is fine
# However we prefer double just in case a word uses
# an apostrophe in it for contractions

# This data type is weird because it isn't just one
# piece of data but rather a collection of letters
# called characters. Strings are called such
# becuase they are just some characters that have
# been stringed together in a line.

# Strings also have operations we can make with them

print("String Operators")
print('######################################################################################')
print("Operator:		Meaning:				Example:")
print("string[x]		get the xth character			'abcde'[1] is 'b'")
print("string[x:y] 		get all the character from xth to yth 	'abcde'[1:3] is 'bc'")
print("string[:y] 		get every character up until yth 	'abcde'[:3] is 'abc'")
print("string[x:]		get every character from xth until end 	'abcde'[3:] is 'de'")
print("len(string)		return the length of the string 	len('abcde') is 5")
print("string+string		join two strings together 		'abc'+'def' is 'abcdef")
print('######################################################################################')
print("")

# Those are the operators for strings

# Booleans

# We covered boolean logic earlier in this course
# so this should be a refresher

print("Boolean Operators")
print('######################################################################################')
print("'and' operator 						Example:")
print("________________________________________________")
print("	A 	| 	B 	|	X 	|")
print("-------------------------------------------------")
print("false		| false		| false		|	False and False is False")
print("-------------------------------------------------")
print("false		| true		| false		|	False and True is False")
print("-------------------------------------------------")
print("true		| false		| false		|	True and False is False")
print("-------------------------------------------------")
print("true		| true		| true		|	True and True is True")
print("________________________________________________")
print("")
print("'or' operator")
print("________________________________________________")
print("	A 	| 	B 	|	X 	|")
print("-------------------------------------------------")
print("false		| false		| false		|	False or False is False")
print("-------------------------------------------------")
print("false		| true		| true		|	False or True is True")
print("-------------------------------------------------")
print("true		| false		| true		|	True or False is True")
print("-------------------------------------------------")
print("true		| true		| true		|	True or True is True")
print("________________________________________________")
print("")
print("'not' operator")
print("________________________________")
print("	A 	|	X 	|")
print("---------------------------------")
print("false		| true		|			not False is True")
print("---------------------------------")
print("true		| false		|			not True is False")
print("________________________________")
print('######################################################################################')
print("")

# These are the boolean operators

# Conversion

# We can convert between the types of values
# using int(), str() and float()
# However there are some rules that apply

# Test these out and see if you can come up
# with the rules that may or may not apply

# >>> print(int(3.9))
# >>> print(str(True))
# >>> print(float("Three point two"))

# QUIZ TIME!!!

# Note some of these will return error so 
# just type in error for those

# >>> int("two")						answer:
# >>> print(str(3+3) + "3")				answer:
# >>> type(3=3)							answer:
# >>> "4" == 4							answer:
# >>> "Python"[4]						answer:
# >>> (3 > 2) or (2 > 3)				answer:
# >>> not "True"						answer:
# >>> 2345[2]							answer:
# >>> str((not True) and (not False))	answer:
# >>> 10 % 3