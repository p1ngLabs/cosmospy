"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# create a collection of distinct telephone numbers from the data set
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
result = dict()

for call in calls:
    for index in [0,1]:
        if call[index] in result:
            result[call[index]] += int(call[-1])
        else:
            result[call[index]] = int(call[-1])

longest_time_spent = max(result.values())
most_time_spent_number = filter(lambda num: result[num] == longest_time_spent, result)
print(most_time_spent_number)

print(f"{most_time_spent_number} spent the longest time, {longest_time_spent} seconds, on the phone during September 2016.")
