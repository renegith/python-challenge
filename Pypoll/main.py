#import currency mod
import locale
#set currency mod
locale.setlocale( locale.LC_ALL, '' )
#import CSV reading mod
import os
import csv
#Define variables
vcounter = 0
c1 = "Khan" 
c2 = "Correy"
c3 = "Li"
c4 = "O'Tooley"
v1 = 0
v2 = 0
v3 = 0
v4 = 0

#open CSV
csvpath = os.path.join('..', 'Pypoll', 'pypoll.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
#Skip first row
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')
#for loop
    for row in csvreader:
        #Total votes
        vcounter = vcounter + 1
        #Votes per candidate
        if row[2] == c1:
            v1 = v1 + 1
        elif row[2] == c2:
            v2 = v2 + 1
        elif row[2] == c3:
            v3 = v3 + 1
        else:
            v4 = v4 + 1
#Winner if
if v1 > v2 and v1 > v3 and v1 > v4:
    Winner = c1
elif v2 > v1 and v2 > v3 and v2 > v4:
    Winner = c2
elif v3 > v1 and v3 > v2 and v3 > v4:
    Winner = c3
else:
    Winner = c4
#Print on terminal
print('Election Results')
print('----------------------------')
print(f'Total votes = {locale.format_string("%d", vcounter, grouping=True)}')
print('----------------------------')
print(f'{c1}: {"{:.2%}".format(v1/vcounter)} ({locale.format_string("%d", v1, grouping=True)})')
print(f'{c2}: {"{:.2%}".format(v2/vcounter)} ({locale.format_string("%d", v2, grouping=True)})')
print(f'{c3}: {"{:.2%}".format(v3/vcounter)} ({locale.format_string("%d", v3, grouping=True)})')
print(f'{c4}: {"{:.2%}".format(v4/vcounter)} ({locale.format_string("%d", v4, grouping=True)})')
print('----------------------------')
print('Winner: ' + (Winner))
#Export to txt
output_file = os.path.join('..', 'Pypoll',"Election Results.txt")
with open(output_file, "w") as text:
    text.write('Election Results'+ "\n")
    text.write('----------------------------'+ "\n")
    text.write(f'Total votes = {locale.format_string("%d", vcounter, grouping=True)}'+ "\n")
    text.write('----------------------------'+ "\n")
    text.write(f'{c1}: {"{:.2%}".format(v1/vcounter)} ({locale.format_string("%d", v1, grouping=True)})'+ "\n")
    text.write(f'{c2}: {"{:.2%}".format(v2/vcounter)} ({locale.format_string("%d", v2, grouping=True)})'+ "\n")
    text.write(f'{c3}: {"{:.2%}".format(v3/vcounter)} ({locale.format_string("%d", v3, grouping=True)})'+ "\n")
    text.write(f'{c4}: {"{:.2%}".format(v4/vcounter)} ({locale.format_string("%d", v4, grouping=True)})'+ "\n")
    text.write('----------------------------'+ "\n")
    text.write('Winner: ' + (Winner)+ "\n")