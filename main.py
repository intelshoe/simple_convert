'''
A simple converter tool.
Converts decimal, hex, binary, and ascii.

Author: mp
'''

# take first value to be converted
print("Convert what type of value?\n")
print("Choose b for binary or d for decimal\n")
convertfrom = str(input())
print("Ok, please enter the value: ")
start_value = int(input())
print(f"Thank you, we will start with {start_value}.\n")

# choose what to convert the value into
print("And what would you like to convert this to?\n")
print("Choose d for decimal or h for hex\n")
convert2 = str(input())

dnum = 0
i = 1
# runs the conversions
if convertfrom == "d" and convert2 == "h":
	print("\n" + hex(start_value))
elif convertfrom == "h":
	pass
elif convertfrom == "b" and convert2 == "d":
	while start_value != 0:
		rem = start_value % 10
		dnum = dnum + (rem*i)
		i = i*2
		start_value = int(start_value/10)

	print("\nEquivalent Decimal Value = ", dnum)
	
elif convertfrom == "a":
	pass
else:
	Print("The input was not correct, please try again.")
	quit()
