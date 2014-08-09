from urllib2 import urlopen
from json import load
import re
import csv
import sqlite3

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()


#Create and Sqlite3 database to store the data

c.execute("CREATE TABLE Restaurant (name text, address text, phone int, cuisine text, eatingOptions text, latitude int, longitude int)")

names = []
addresses = []
phoneNumbers = []
cuisines = []
eatingOptions = []


def getDataFromCSV(names,addresses,phoneNumbers,cuisines,eatingOptions):

	with open('data.csv','rU') as f:
	    columns = csv.reader(f) # imports all the columns.
	     
	    for row in columns:
	     	# print row[0] # row[0] will give the first item of the first column, the for loop will iterate over it and print all the rows
	    		
	    	names.append(row[0]) # takes a row from column 0 and adds it to 'name' array/list
	     	addresses.append(row[1])
	     	phoneNumbers.append(row[2])
	     	cuisines.append(row[3])
	     	eatingOptions.append(row[4])


def addPlusSignBetweenWords(name,address):

		# Create an array for name with each word as an item
		name = re.compile('\w+').findall(name)

		nameWithPlusBetweenWords = []

		# Create a new list and add '+' between each word (each item in the list)

		for word in name:
			
			nameWithPlusBetweenWords.append(word)
			nameWithPlusBetweenWords.append("+")

		# Create an array for address with each word as an item

		address = re.compile('\w+').findall(address)

		addressWithPlusBetweenWords = []

		# Create a new list and add '+' between each word (each item in the list)

		for word in address:

			addressWithPlusBetweenWords.append(word) 
			
			addressWithPlusBetweenWords.append("+")
			
		# Remove the last item in the list, which is '+'

		addressWithPlusBetweenWords.pop() 

		# Take the two lists and join them

		b = nameWithPlusBetweenWords + addressWithPlusBetweenWords

		# Take the new list 'b' and create a string

		b = ''.join(b)

		return b

getDataFromCSV(names,addresses,phoneNumbers,cuisines,eatingOptions)








