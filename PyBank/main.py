#import currency mod
import locale
#set currency mod
locale.setlocale( locale.LC_ALL, '' )

#import CSV reading mod
import os
import csv

#Name variables
mcounter = 0
totalpnl = 0
avgrevchange = 0
prevrev = 0
revchange = []
months = []

#open CSV
csvpath = os.path.join('..', 'Pybank', 'pybank.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
#Skip first row
    csv_header = next(csvfile)
    print(f'Header: {csv_header}')
#for loop
    for row in csvreader:
#Sum Total months
        mcounter = mcounter + 1
        months.append(row[0])
#Sum Total PnL
        totalpnl = totalpnl + int(row[1])
#Avg Rev Change
        currentrev = int(row[1])
        if mcounter > 1:
            avgrevchange = currentrev - prevrev
            revchange.append(avgrevchange)
        prevrev = currentrev
allchanges = sum(revchange)
avgrevchange = allchanges / (mcounter-1)
#Greatest increase and decrease on profits
ginc=max(revchange)
gdec=min(revchange)
gincindx = revchange.index(ginc)
gdecindx = revchange.index(gdec)
gincmonth = months[gincindx+1]
gdecmonth = months[gdecindx+1]   
#Print on terminal    
print('Financial Analysis')
print('----------------------------')
print(f'Total months = {mcounter}')
print(f'Total P&L = {locale.currency(totalpnl,grouping=True)}')
print(f'Average change in P&L = {locale.currency(avgrevchange,grouping=True)}')
print(f'Greatest increase in profits = {gincmonth} {locale.currency(ginc,grouping=True)}')
print(f'Greatest decrease in profits = {gdecmonth} {locale.currency(gdec,grouping=True)}')
#Export to txt
output_file = os.path.join('..', 'Pybank',"Financial Analysis.txt")
with open(output_file, "w") as text:
    text.write('Financial Analysis'+ "\n")
    text.write('----------------------------'+ "\n")
    text.write(f'Total months = {mcounter}'+ "\n")
    text.write(f'Total P&L = {locale.currency(totalpnl,grouping=True)}'+ "\n")
    text.write(f'Average change in P&L = {locale.currency(avgrevchange,grouping=True)}'+ "\n")
    text.write(f'Greatest increase in profits = {gincmonth} {locale.currency(ginc,grouping=True)}'+ "\n")
    text.write(f'Greatest decrease in profits = {gdecmonth} {locale.currency(gdec,grouping=True)}'+ "\n")