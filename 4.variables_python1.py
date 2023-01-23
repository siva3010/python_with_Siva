my_income=100    #my_income is variable 
tax_raete=0.5     #my_tax_rate is variable

my_tax = my_income * tax_raete

print(my_tax)

print(type(my_tax))

#variable name

my_name="siva"

print(my_name)
#variable can not contain stating number,white space,-

#assigning multiple variable
x,y,z=10,10,10
print(x,y,z)

#Global variable

x1="siva"

def myname():
    print(x1+"prakash")
myname()    

x2="siva"
def my():
    global x
    x="prakash"
my()
print("x"+x2)    