#!/usr/bin/python

import json
def decode_modify_print_encode_json_string():
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'                   # It's not json data; just a json string rather. See the see quotes surrounding it
    decoded_data = json.loads(json_string)                                          # Convert it to json                                        

    print decoded_data["first_name"]                                                # Note that in case of json; data can be retrieved using "get" or the same way as in dictionary                                             
    print decoded_data.get("first_name")
    decoded_data["middle_name"] = "kumar"                                           # Add a new key

    print decoded_data
    for k in decoded_data.keys():                                                   # printing key values
        print k, decoded_data[k]

    json_encoded = json.dumps(decoded_data)                                         # Convert the json data back to string, a json string
    print json_encoded

def read_txt_write_json():
    data = ""
    
    with open('sample.txt', 'r') as fp:         #data = json.load(open('sample.json'))
        data = json.load(fp)                    # Note the difference. For string it's "loads" while in case of reading a file it's "read"

    data["new_data"] = "value to be added"
    
    with open('data.json', 'w') as f:           # Writing JSON data
        json.dump(data, f)

import urllib2
def get_json_data_from_url():
    response = urllib2.urlopen('http://myurl.com/?get_data=json')
    json_string = response.read()
    decoded_data = json.loads(json_string)                    

import pandas as pd
def read_excel_file(xlsFile):
    #xlsFile="/spare/testdata/test.xlsx"
    xl = pd.ExcelFile(xlsFile)

    sheet_name='Certifications'
    df1 = xl.parse(sheet_name)
    print df1.head                                          # Prints header(or column names) of sheet 'Certifications'
    print xl.sheet_names

    xls = pd.read_excel(xlsFile, sheetname=sheet_name)      # To read a shpecific sheet

    print("Column headings:")
    print(xls.columns)

    values = xls['Level'].values                            # get the values for a given column
    print values

# How to run bash command in python
'''
subprocess, os.system() and os.pipe()? Why subprocess is better?
subprocess.Popen() is strict superset of os.system().The subprocess module is newer and generally more powerful because It provides greater control of how commands are executed.

So, os.system() is suitable when you just want to execute a program in a subshell and get the return code. subprocess.call and other functions from subprocess come handy if you need more control.
os.system is equivalent to Unix system command, while subprocess was a helper module created to provide many of the facilities provided by the Popen commands with an easier and controllable
interface. Those were designed similar to the Unix Popen command.
system() executes a command specified in command by calling /bin/sh -c command, and returns after the command has been completed
where as popen() function opens a process by creating a pipe, forking, and invoking the shell.
If you are thinking, which one to use, then use subprocess definitely because you you have all facilities for execution, plus additional control over the process.

'''  
import subprocess
def run_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    (out, err) = process.communicate()
    exitcode = process.returncode

# List all python files in a directory
import os
from fnmatch import fnmatch
def allPythonFilesInDir(dir):
    pattern = "*.py"
    for path, subdirs, files in os.walk(dir):
        for name in files:
            if fnmatch(name, pattern):
                print os.path.join(path, name)

'''
Read two files and copy the contents to a third file and count the no of lines
r  - read file 
w  - edit and write new information to the file (any existing files with the same name will be erased when this mode is activated). Creates file if it doesn't exist
a  - add new data to the end of the file
r+ - read and write; it doesn't create file it that doesn't exist
'''
def readFilesCopyToAnother():
    fileName1 = "/tmp/firstFile.txt"
    fileName2 = "/tmp/secondFile.txt"
    fileName3 = "/tmp/thirdFile.txt"

    content1 = ""
    content2 = ""

    with open(fileName1, "r") as f:
        content1 = f.read()

    with open(fileName2, "r") as f:
        content2 = f.read()
        print "No of lines in third file = ", len(f.readlines())  # f.read().split() is similar to f.readlines(). It's a list with all the lines as elements

    with open(fileName3, "w") as f:
        f.write(content1)
        f.write(content2)
        f.write("Hello")

import shutil
def deleteFileAndDir():
    if os.path.exists("fileName"):
        os.remove("fileName")               # Deletes file
    os.rmdir("emptyDirName")                # Deletes empty directory
    shutil.rmtree("dirName")                # Removes the specified directory, all subdirectories, and all files. 

# Connect to MySQL
import MySQLdb
# Open database connection
def connectMySQL():
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()                                                    # prepare a cursor object using cursor() method
    cursor.execute("SELECT VERSION()")                                      # execute SQL query using execute() method.
    data = cursor.fetchone()                                            
    print "Database version : %s " % data
    db.close()

def connectSQLandInsert():
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def connectSQLfetchAll():
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
    except:
        print "Error: unable to fecth data"
    db.close()

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print "Move disk 1 from rod",from_rod,"to rod",to_rod
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print "Move disk",n,"from rod",from_rod,"to rod",to_rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def printFloydTriangle(n):
    i = 0
    j = 0
    val = 1

    for i in xrange(1, n+1):
        for j in xrange(1, i+1):
            print val,
            val += 1
        print ""

def checkLeapYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))   #Year is multiple of 400 or Year is multiple of 4 and not multiple of 100.

# Program for Sum the digits of a given number
def getSum(n):
    Sum = 0
    while (n != 0):
        Sum = Sum + n % 10
        n = n/10
    return Sum

# print nos till n without using loop
# Time complexity: O(n)
def printNos(n):
    if n > 0:
        printNos(n-1)
        print n,

# find angle between hour and minute hands
def calcAngle(h,m):
        if (h < 0 or m < 0 or h > 12 or m > 60):
            print 'Wrong input'
         
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            
        hour_angle = 0.5 * (h * 60 + m)         # Calculate the angles moved by hour and minute hands with reference to 12:00
        minute_angle = 6 * m
        angle = abs(hour_angle - minute_angle)
        angle = min(360 - angle, angle)         # Return the smaller angle of two possible angles
         
        return angle

'''
Count Possible Decodings of a given Digit Sequence

LLet 1 represent 'A', 2 represents 'B', etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.

Examples:
Input:  digits[] = "121"
Output: 3
The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
The possible decodings are "ABCD", "LCD", "AWD"

An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and there are no leading 0's, no extra trailing 0's and no two or more consecutive 0's.

This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence. We initialize the total count of decodings as 0. We recur for two subproblems.
 1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
 2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add the result to total count.
 The time complexity of above the code is exponential. If we take a closer look at the above program, we can observe that the recursive solution is similar to Fibonacci Numbers.
 Therefore, we can optimize the above solution to work in O(n) time using Dynamic Programming. https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
'''
def countDecoding(digits, n):
    if (n == 0 or n == 1):
        return 1

    count = 0

    if (int(digits[n-1]) > 0):                                                          # If the last digit is not 0, then last digit must add to the number of words
        count =  countDecoding(digits, n-1)

    if (int(digits[n-2]) == 1 or (int(digits[n-2]) == 2 and int(digits[n-1]) < 7) ):    # If the last two digits form a number smaller than or equal to 26, then consider last two digits and recur
        count +=  countDecoding(digits, n-2)

    return count

def swap():
  x = 10
  y = 5

  temp = x
  x = y
  y = temp
  print "After Swapping: x = %d, y = %d" %(x, y)
  return 0

# Swap without using third variable. See below definitions
def swap_using_addition_subtraction():
  x = 10
  y = 5

  x = x + y;  # x now becomes 15
  y = x - y;  # y becomes 10
  x = x - y;  # x becomes 5

  print "After Swapping: x = %d, y = %d" %(x, y)
  return 0

def swap_using_multiplication_division():
  x = 10
  y = 5

  # Code to swap 'x' and 'y'
  x = x * y  #// x now becomes 50
  y = x / y  #// y becomes 10
  x = x / y  #// x becomes 5

  print "After Swapping: x = %d, y = %d" %(x, y)
  return 0

def swap_using_xor():
  x = 10
  y = 5

  # Code to swap 'x' (1010) and 'y' (0101)
  x = x ^ y  # x now becomes 15 (1111)
  y = x ^ y  # y becomes 10 (1010)
  x = x ^ y  # x becomes 5 (0101)

  print "After Swapping: x = %d, y = %d" %(x, y)

  return 0

#import paramiko, sys
def doSSHrunCommand(cmd):
    nbytes = 4096
    hostname = 'hostname'
    port = 22
    username = 'username'
    password = 'password'
    command = 'ls'

    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)

    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print 'exit status: ', session.recv_exit_status()
    print ''.join(stdout_data)
    print ''.join(stderr_data)

    session.close()
    client.close()
    digits = "1234";
    n = len(digits);
    print countDecoding(digits, n)

# The Singleton Pattern implemented with Python (Python recipe)
# http://code.activestate.com/recipes/52558-the-singleton-pattern-implemented-with-python/
class Singleton:
    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Singleton.__instance is None:
            # Create and remember instance
            Singleton.__instance = Singleton.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

# Test it
s1 = Singleton()
print id(s1), s1.spam()

s2 = Singleton()
print id(s2), s2.spam()

# Sample output, the second (inner) id is constant:
# 8172684 8176268
# 8168588 8176268

h = 9
m = 60
print('Angle ', calcAngle(h,m))

n = 687
print getSum(n)
'''
Floyd's triangle
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21
'''            
printFloydTriangle(6)

'''
Program for Tower of Hanoi
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
 1) Only one disk can be moved at a time.
 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
 3) No disk may be placed on top of a smaller disk.

Approach : 
Take an example for 2 disks :
Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'.

Step 1 : Shift first disk from 'A' to 'B'.
Step 2 : Shift second disk from 'A' to 'C'.
Step 3 : Shift first disk from 'B' to 'C'.

The pattern here is :
Shift 'n-1' disks from 'A' to 'B'.
Shift last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C'
'''
n = 4
TowerOfHanoi(n, 'A', 'C', 'B') 

decode_modify_print_encode_json_string()
read_txt_write_json()
# Print environment variable
import os
#print os.environ
