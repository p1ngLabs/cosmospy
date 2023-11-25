"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    numbers_in_texts = set()
    for text in texts:
        numbers_in_texts.add(text[0])
        numbers_in_texts.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    numbers_in_calls = set()
    for call in calls:
        numbers_in_calls.add(call[0])
        numbers_in_calls.add(call[1])

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
distinct_numbers = numbers_in_texts.union(numbers_in_calls)
count = len(distinct_numbers)
print(f"There are {count} different telephone numbers in the records.") # 570
