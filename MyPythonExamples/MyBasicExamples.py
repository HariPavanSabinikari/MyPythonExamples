import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#List Example
thislist = ["apple", "banana", "cherry"]
print(thislist)

#To import 
#Camel case importing
import camelcase

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))

#Try catch Exception..Change x to another variable which is not declared.
try:
    print(x)
except:
    print("An exception occurred")
    
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#below code explains how to connect to oracle.
import cx_Oracle
#we we are using oracle wallet.
db = cx_Oracle.connect("/@CLDW_MFG_DEV")
cursor=db.cursor()
r=cursor.execute("SELECT COUNT(*) as REC_CUNT from table_1")
for REC_CUNT in cursor:
    print(REC_CUNT)
