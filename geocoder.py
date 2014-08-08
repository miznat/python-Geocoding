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