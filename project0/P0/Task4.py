"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from typing import Set

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
numbers_that_make_ongoing_calls = set()
numbers_that_receive_calls = set()
numbers_that_text = set()

for call in calls:
    numbers_that_make_ongoing_calls.add(call[0])
    numbers_that_receive_calls.add(call[1])

for txt in texts:
    numbers_that_text.add(txt[0])
    numbers_that_text.add(txt[1])
    

def get_possible_telemarketers(numbers: Set[str]) -> Set[str]:
    for num in numbers.copy():
        # exclude numbers that never receive incoming calls
        if num not in numbers_that_receive_calls:
            numbers.remove(num)
        # exclude numbers that never text
        elif num not in numbers_that_text:
            numbers.remove(num)

    return numbers
    
result = get_possible_telemarketers(numbers_that_make_ongoing_calls)
print("These numbers could be telemarketers: ")
for num in result:
    print(num)
