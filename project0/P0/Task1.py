"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    numbers_in_texts = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    numbers_in_calls = set()

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
distinct_numbers = set()

for text in texts:
    distinct_numbers.add(text[0])
    distinct_numbers.add(text[1])

for call in calls:
    distinct_numbers.add(call[0])
    distinct_numbers.add(call[1])

print(f"There are {len(distinct_numbers)} different telephone numbers in the records.") # 570
