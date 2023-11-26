"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# create a collection of distinct telephone numbers from the data set
distinct_numbers = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        # number that makes a call
        distinct_numbers.add(call[0])
        # number that receives a call
        distinct_numbers.add(call[1])

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
result = dict()
for number in distinct_numbers:
    time = 0
    for call in calls:
        if number in call:
            # add time to total time spent on phone, whether calling or answering
            time += int(call[-1])
    result[number] = time

longest_time_spent = max(result.values())
most_time_spent_number = list(filter(lambda num: result[num] == longest_time_spent, result))[0]

print(f"{most_time_spent_number} spent the longest time, {longest_time_spent} seconds, on the phone during September 2016.")
