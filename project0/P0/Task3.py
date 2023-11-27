"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
BANGALORE_CODE = '(080)'

print("--- Part A ---")
def get_area_codes_and_mobile_prefixes(number: str):
    TELEMARKETERS_PREFIX = '140'
    # telemarketers' numbers
    if number.startswith(TELEMARKETERS_PREFIX):
        return TELEMARKETERS_PREFIX
    # area code prefixes that is enclosed in parentheses
    if number.startswith('(0'):
        return number[1:number.index(')')]
    # mobile prefixes which have four digits
    if ' ' in number.strip() and int(number[0]) in [7,8,9]:
        return number[:4]

calls_from_Bangalore = 0
calls_from_Bangalore_to_Bangalore = 0
result = set()
for call in calls:
    if BANGALORE_CODE in call[0]:
        result.add(get_area_codes_and_mobile_prefixes(call[1]))
        calls_from_Bangalore += 1
        if BANGALORE_CODE in call[1]:
            calls_from_Bangalore_to_Bangalore += 1

print("The numbers called by people in Bangalore have codes:")
for code in sorted(result):
    print(code)

print("\n--- Part B ---")
percentage = calls_from_Bangalore_to_Bangalore / calls_from_Bangalore * 100
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")