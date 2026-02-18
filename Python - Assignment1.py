# Python Assignment 1

# Q1
name = ''' Hi How are you?
Starterd learning python.
It's really interesting.''' 

print(name[:] )
print(name[-10:-5])
print(name[3:12])
print(name[12:3])
print(name[5,6]) 
print(name[-4:-12:-1])
print(name[-4:-12])
print(name[::2]) #--> take entire string and just every 2nd character
print(name[::-2]) #--> reverse entire string and just every 2nd character

#Q2.

l1 = ['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(l1[::-2])
print(l1[::3])
print(l1[:])

#d.	How to extract  value “Happy” based on index and negative index
l1 = ['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(l1[-2])
print(l1.index('Happy'))

#e.	How to check type of data in list at 4th position
l1 = ['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(type(l1[3]))

# f.	Extract values for 100, 300, 400 
l1 = ['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(l1[5:8])


##Q3.

L2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success'] 
print(L2[4])
print(L2[1:5])
print(L2[7])
print(L2[7][2])
print(L2[7][2:])
print(L2[ : 3])
print(L2[3:])


#Q4.	From the above l2 value 'b' must be changed to 'BEE'.
L2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success'] 
L2[4][1] = 'BEE'
print(L2)


# Q5.	From l2 “BEE” has to discard.
L2 =[1,2,3,5,['a', 'BEE', 'work hard'],100 , 200, 'Success'] 
L2[4].remove('BEE')
print(L2)


# Q6.	In l2 add a dictionary at the end {'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']}
L2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success'] 
L2.append({'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']})
print(L2)


#Q7.	From l2 extract insect information.
l2 = [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
print(l2[8]['insect']) #-> []index []key
print(l2[8]['bird'])

#Q8.	Create a dictionary d1 = {'a':10, 'b':20, 'c' : 30} and 
# add the d1 at 2nd position of l2
d1 = {'a':10, 'b':20, 'c' : 30}
l2 = [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
l2.insert(1, d1)
print(l2)

#Q9.	Based on new l2 created here extract the value 10 
# from l2 dictionary.

l2 = [1, {'a': 10, 'b': 20, 'c': 30}, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
print(l2[1]['a'])

#Q 10.

L2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success', (200,300, 'Hundreds')] 

print(L2[4][2])
print(L2[5][:])
#print(L2[2] [:])
print(L2[1:5])
print(L2[5])
print(L2[5][3:-1])
print(L2[-1])
#print(L2[-4, -3])
print(L2[-4: -10])
print(L2[7][2])
print(L2[-7][2:])
print(L2[ :- 3])
print(L2[-3:])



# Q11.	Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail

marks = input("Enter marks: ")
if marks.isdigit():
    marks = float(marks)
    if marks > 100 or marks < 0:
        print("Pls enter correct marks.")
    elif marks > 80 :
        print("Distinction")
    elif marks > 70:
        print("First class")
    elif marks > 50:
        print("Second class")
    elif marks > 35:
        print("Pass")
    else:
        print("Fail")     
else:
    print("Enter just digits.")


# Q12.	Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are  A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are  A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are  A = 8% , B=6%, C= 4%, D = no increment
# If salary upto 23 lpa then increament based on ratings are  A = 7% , B=5%, C= 4%, D=no


salary = int(input("Enter salary: "))
rating = input("Enter rating: ").capitalize()

if salary > 0 and rating in ['A', 'B', 'C', 'D']:
    if salary <= 500000:
        if rating == 'A':
            print("16 percent increment which is ", salary*0.16)
        elif rating == 'B':
            print("12 percent increment which is ", salary*0.12)
        elif rating == 'C':
            print("10 percent increment which is ", salary*0.10)
        elif rating == 'D':
            print("6 percent increment which is ", salary*0.06)
    elif salary <= 1000000:
        if rating == 'A':
            print("14 percent increment which is ", salary*0.14)
        elif rating == 'B':
            print("10 percent increment which is ", salary*0.10)
        elif rating == 'C':
            print("8 percent increment which is ", salary*0.08)
        elif rating == 'D':
            print("6 percent increment which is ", salary*0.06)
    elif salary <= 1500000:
        if rating == 'A':
            print("8 percent increment which is ", salary*0.08)
        elif rating == 'B':
            print("6 percent increment which is ", salary*0.06)
        elif rating == 'C':
            print("4 percent increment which is ", salary*0.04)
        elif rating == 'D':
            print("No increment")
    elif salary <= 2300000:
        if rating == 'A':
            print("7 percent increment which is ", salary*0.07)
        elif rating == 'B':
            print("5 percent increment which is ", salary*0.05)
        elif rating == 'C':
            print("4 percent increment which is ", salary*0.04)
        elif rating == 'D':
            print("No increment")

else:
    print("Enter appropriate salary / rating")



# 13.	Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. 
# For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics.
# Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)


L1 = ["HR", "Finance", "Marketing", "DS"]
BASE_FEE = 200000
HOSTEL_FEE = 200000
FOOD_PER_MONTH = 2000
TRANSPORT_PER_SEM = 13000
 
print("Available Courses:", L1)
 
subject = input("Enter subject: ").upper()
analytics = input("Analytics (Y/N): ").upper()
hostel = input("Hostel (Y/N): ").upper()
food_months = int(input("Food (How many months?): "))
transport = input("Transportation (semester/annual): ").lower()
 
total_fee = 0
 
if subject not in L1:
    print("Invalid Subject Selected")
    exit()
 
course_fee = BASE_FEE
 
if analytics == "Y":
    if subject in ["HR", "Marketing"]:
        course_fee += BASE_FEE * 0.10
    else:
        print("Analytics is not available for this subject")
 
total_fee += course_fee
 
if hostel == "Y":
    total_fee += HOSTEL_FEE
 
total_fee += food_months * FOOD_PER_MONTH
 
if transport == "semester":
    total_fee += TRANSPORT_PER_SEM
elif transport == "annual":
    total_fee += TRANSPORT_PER_SEM * 2
 

print("\n")
print("Subject:", subject)
print("Course Fee: Rs.", int(course_fee))
print("Total Annual Cost: Rs.", int(total_fee))




#----------------
# Using functions

L1 = ["HR", "Finance", "Marketing", "DS"]
BASE_FEE = 200000
HOSTEL_FEE = 200000
FOOD_PER_MONTH = 2000
TRANSPORT_PER_SEM = 13000


def CalculateFees(subject, analytics):
    fee = BASE_FEE

    if analytics == 'Y':
        if subject in ["HR", "Marketing"]:
            fee += BASE_FEE * 0.10
    else:
        print("Analytics is not available for this subject")

    return fee
    

def CalculateHostelFee(hostel):
    if hostel == "Y":
        return HOSTEL_FEE
    return 0


def CalculateFoodFee(months):
    return months * FOOD_PER_MONTH


def CalculateTransportFee(transport_type):
    if transport_type == "semester":
        return TRANSPORT_PER_SEM
    elif transport_type == "annual":
        return TRANSPORT_PER_SEM * 2
    else:
        return 0



print("Available Courses:", L1)

subject = input("Enter subject: ").upper()
analytics = input("Analytics (Y/N): ").upper()
hostel = input("Hostel (Y/N): ").upper()
food_months = int(input("Food (How many months?): "))
transport = input("Transportation (semester/annual): ").lower()

if subject not in L1:
    print("Invalid Subject Selected")
    exit()

total_fee = 0

course_fee = CalculateFees(subject, analytics)
hostel_fee = CalculateHostelFee(hostel)
food_fee = CalculateFoodFee(food_months)
transport_fee = CalculateTransportFee(transport)

total_fee = course_fee + hostel_fee + food_fee + transport_fee

print("\nSubject:", subject)
print("Course Fee: Rs.", int(course_fee))
print("Total Annual Cost: Rs.", int(total_fee))




#----------------
# above code using OOPS
 
class CollegeFee:
 
    L1 = ["HR", "Finance", "Marketing", "DS"]
    BASE_FEE = 200000
    HOSTEL_FEE = 200000
    FOOD_PER_MONTH = 2000
    TRANSPORT_PER_SEM = 13000
 
    def __init__(self, subject, analytics, hostel, food_months, transport):
        self.subject = subject
        self.analytics = analytics
        self.hostel = hostel
        self.food_months = food_months
        self.transport = transport
        self.total_fee = 0
        self.course_fee = 0
 
    def calculate_course_fee(self):
        if self.subject not in CollegeFee.L1:
            print("Invalid Subject Selected")
            exit()
 
        self.course_fee = CollegeFee.BASE_FEE
 
        if self.analytics == "Y":
            if self.subject in ["HR", "Marketing"]:
                self.course_fee += CollegeFee.BASE_FEE * 0.10
            else:
                print("Analytics is not available for this subject")
 
        self.total_fee += self.course_fee
 
    def add_hostel_fee(self):
        if self.hostel == "Y":
            self.total_fee += CollegeFee.HOSTEL_FEE
 
    def add_food_fee(self):
        self.total_fee += self.food_months * CollegeFee.FOOD_PER_MONTH
 
    def add_transport_fee(self):
        if self.transport == "semester":
            self.total_fee += CollegeFee.TRANSPORT_PER_SEM
        elif self.transport == "annual":
            self.total_fee += CollegeFee.TRANSPORT_PER_SEM * 2
 
    def display_summary(self):
        print("\n------ Fee Summary ------")
        print("Subject:", self.subject)
        print("Course Fee: ₹", int(self.course_fee))
        print("Total Annual Cost: ₹", int(self.total_fee))
 
 
 
print("Available Courses:", CollegeFee.L1)
 
subject = input("Enter subject: ")
analytics = input("Analytics (Y/N): ").upper()
hostel = input("Hostel (Y/N): ").upper()
food_months = int(input("Food (How many months?): "))
transport = input("Transportation (semester/annual): ").lower()
 
student = CollegeFee(subject, analytics, hostel, food_months, transport)
 
student.calculate_course_fee()
student.add_hostel_fee()
student.add_food_fee()
student.add_transport_fee()
student.display_summary()
 


#--------

# 14.	Digitalize the book allotment process for school. Charges are mentioned here in the given table:

total = 0

std = int(input("Enter Standard (1-10): "))

if 1 <= std <= 4:
    standard = "1-4"
elif 5 <= std <= 8:
    standard = "5-8"
elif 9 <= std <= 10:
    standard = "9-10"
else:
    print("Invalid Standard")
    exit()


books = {
    "1-4": {
        "hindi": 60, "marathi": 60, "english": 80,
        "science": 90, "maths": 100
    },
    "5-8": {
        "hindi": 100, "marathi": 100, "english": 100,
        "science": 120, "maths": 140
    },
    "9-10": {
        "hindi": 150, "marathi": 150, "english": 150,
        "science": 200, "maths": 250
    }
}


choice = input("Do you want books? (yes/no): ").lower()

if choice == "yes":

    print("Subjects: Hindi Marathi English Science Maths")

    subjects = input(
        "Enter subjects separated by space: "
    ).lower().split()

    for sub in subjects:
        if sub in books[standard]:
            total += books[standard][sub]
        else:
            print("Invalid subject skipped:", sub)


notebooks = {
    "1": 40,   # square 100
    "2": 70,   # square 200
    "3": 30,   # 4 lines 100
    "4": 50,   # 4 lines 200
    "5": 30,   # single 100
    "6": 50,   # single 200
    "7": 100,  # A4 100
    "8": 180   # A4 200
}

choice2 = input("Do you want notebooks? (yes/no): ").lower()

if choice2 == "yes":

    print("""
1 Square 100 pages
2 Square 200 pages
3 Four lines 100 pages
4 Four lines 200 pages
5 Single line 100 pages
6 Single line 200 pages
7 A4 100 pages
8 A4 200 pages
""")

    nbs = input(
        "Enter notebook numbers separated by space: "
    ).split()

    for nb in nbs:
        if nb in notebooks:
            total += notebooks[nb]
        else:
            print("Invalid notebook skipped:", nb)

print("\nTotal Amount to Pay =", total)


# -------------------
#  Using functions

def user_input(*s):
    std = input('Enter which standard: ')
    book = input('Enter the subject: ')
    b_quant = input('Quantity: ')
    return dict({
        "Standard" : std,
        "Subject" : book,
        "Quantity" : b_quant
    })

print(user_input())
 
 
def get_standard():
    s = int(input("Enter Standard (1-10): "))
    if 1 <= s <= 4:
        return "1-4"
    elif 5 <= s <= 8:
        return "5-8"
    elif 9 <= s <= 10:
        return "9-10"
    else:
        print("Invalid standard")
        return None
 
 
def get_books_total(standard, book_dict):
    total = 0
    choice = input("Do you want to buy books? (yes/no): ").lower()
 
    if choice == "yes":
        print("Available books: Hindi Marathi English Science Maths")
        subjects = input(
            "Enter the books you want (separated by space): "
        ).lower().split()
 
        for sub in subjects:
            if sub in book_dict[standard]:
                total += book_dict[standard][sub]
            else:
                print(f"Invalid subject skipped: {sub}")
 
    return total
 
 
def get_notebooks_total(notebook_dict):
    total = 0
    choice = input("Do you want to buy notebooks? (yes/no): ").lower()
 
    if choice == "yes":
        notebooks = input(
            """
Choose notebooks:
1 square 100 pages
2 square 200 pages
3 4lines 100 pages
4 4lines 200 pages
5 single_line 100 pages
6 single_line 200 pages
7 A4 notebook 100 pages
8 A4 notebook 200 pages
 
Enter notebook numbers (separated by space):
"""
        ).split()
 
        for nb in notebooks:
            if nb in notebook_dict:
                total += notebook_dict[nb]
            else:
                print(f"Invalid notebook skipped: {nb}")
 
    return total
 
 
def BookAmount():
    book_dict = {
        "1-4": {
            "hindi": 60, "marathi": 60, "english": 80,
            "science": 90, "maths": 100
        },
        "5-8": {
            "hindi": 100, "marathi": 100, "english": 100,
            "science": 120, "maths": 140
        },
        "9-10": {
            "hindi": 150, "marathi": 150, "english": 150,
            "science": 200, "maths": 250
        }
    }
 
    notebook_dict = {
        "1": 40, "2": 70, "3": 30, "4": 50,
        "5": 30, "6": 50, "7": 100, "8": 180
    }
 
    standard = get_standard()
    if standard is None:
        return
 
    total = 0
    total += get_books_total(standard, book_dict)
    total += get_notebooks_total(notebook_dict)
 
    print(f"\nTotal amount to pay: ₹{total}")
 
 
BookAmount()
 


#----------------
# Using oops

class BookAllotment:

    def __init__(self):

        self.book_dict = {
        "1-4": {
            "hindi": 60, "marathi": 60, "english": 80,
            "science": 90, "maths": 100
        },
        "5-8": {
            "hindi": 100, "marathi": 100, "english": 100,
            "science": 120, "maths": 140
        },
        "9-10": {
            "hindi": 150, "marathi": 150, "english": 150,
            "science": 200, "maths": 250
        }
    }

        self.notebook_dict = {
        "1": 40, "2": 70, "3": 30, "4": 50, "5": 30, "6": 50, "7": 100, "8": 180
    }


    def get_standard(self):

        s = int(input("Enter Standard (1-10): "))

        if 1 <= s <= 4:
            return "1-4"

        elif 5 <= s <= 8:
            return "5-8"

        elif 9 <= s <= 10:
            return "9-10"

        else:
            print("Invalid standard")
            return None


    def get_books_total(self, standard):

        total = 0

        choice = input("Do you want to buy books? (yes/no): ").lower()

        if choice == "yes":

            print("Available books: Hindi Marathi English Science Maths")

            subjects = input(
                "Enter subjects separated by space: "
            ).lower().split()

            for sub in subjects:

                if sub in self.book_dict[standard]:
                    total += self.book_dict[standard][sub]

                else:
                    print("Invalid subject skipped:", sub)

        return total


    def get_notebooks_total(self):

        total = 0

        choice = input("Do you want to buy notebooks? (yes/no): ").lower()

        if choice == "yes":

            print("""
1  square 100 pages
2  square 200 pages
3  4lines 100 pages
4  4lines 200 pages
5  single_line 100 pages
6  single_line 200 pages
7  A4 notebook 100 pages
8  A4 notebook 200 pages
""")

            notebooks = input(
                "Enter notebook numbers: "
            ).split()

            for nb in notebooks:

                if nb in self.notebook_dict:
                    total += self.notebook_dict[nb]

                else:
                    print("Invalid notebook skipped:", nb)

        return total


    def generate_bill(self):

        standard = self.get_standard()

        if standard is None:
            return

        total = 0

        total += self.get_books_total(standard)
        total += self.get_notebooks_total()

        print("\nTotal amount to pay:", total)



b = BookAllotment()
b.generate_bill()

# ---------------


# Type Casting 
# 17.	Create a=100 
# •	Convert a to string 
# •	Convert a to list    
# •	Convert a to tuple  
# •	Convert a to dict 
# •	Convert a to set 
# •	Convert to float 
# Observe the errors and note it down for all conversions. 

a = 100
print(str(a))
print(float(a))
print(list(a)) #--> error 'int is not iterable'
print(tuple(a))#--> error 'int is not iterable'
print(dict(a))#--> error 'int is not iterable'
print(set(a))#--> error 'int is not iterable'
 
# 8.	Create city = “Pune” 
# •	Convert to int     
# •	Convert float 
# •	Convert list  
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	Obsert errors and note it down for all conversions 

city = "Pune"
print(int(city)) #-> ValueError: invalid literal for int() with base 10: 'Pune'
print(float(city)) #-> ValueError: could not convert string to float: 'Pune'
print(list(city))
print(tuple(city))
print(dict(city)) #-> ValueError: dictionary update sequence element #0 has length 1; 2 is required
print(set(city))


# 9.	Create a list as marks = [20,18,15,17,18] 
# •	Convert to int 
# •	Convert float 
# •	Convert list 
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	observe : errors and note it down for all conversions 

marks = [20,18,15,17,18]
print(int(marks)) #-> TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(float(marks)) #-> TypeError: float() argument must be a string or a real number, not 'list'
print(list(marks))
print(tuple(marks))
print(dict(marks)) #-> TypeError: cannot convert dictionary update sequence element #0 to a sequence
print(set(marks))


# List operations 
# 10.	Create the empty list snames 
# •	 Add value 20 in the list using append 
# •	 Add value 30 in the list using extend 
# •	Add values in the list using append 
# •	Add value “WORK" in the list using extend 
# •	 Create a new list combo having the values [1, 'a', 'b' ,2 , 3] 
# •	Add sname to combo using addition operator 
# •	Add combo to snames using append 
# •	Add combo to snames using extend. 


snames = []
snames.append(20)
snames.extend([30])
snames.append(40)
snames.extend(['Work'])
print(snames)
combo = [1, 'a', 'b' ,2 , 3]
print(combo+snames)
combo.append(snames)
combo.extend(snames)
print(combo)

# 11.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 

l1 = [1,3,5]
l2 = [2,4,6,8,10,12,14]
l2.insert(4,l1)
print(l2)

# 12.	Collection is the list having values [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]
#  if the data is in integer or float then multiply with 5.  
# •	From the collection delete the record for “Nisha” 
# •	Find the location of 20.50 


l1 = [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]

for i in range(len(l1)):
    if type(l1[i]) == int or type(l1[i]) == float:
        l1[i] = l1[i]*5
print(l1)

# 13.	Create a comprehensive list for square upto 10 

squares = [i ** 2 for i in range(0,11)]
print(squares)

# 14.	Create the comprehensive list to find number divisible by 13 till 200

num = [i for i in range(0,200) if i % 13 == 0]
print(num)

# 15.	Create the list which is divisible by 4 from 300 to 400  

num = [i for i in range(300,400) if i % 4 == 0]
print(num)

# 16.	Create a comprehensive list to generate list up to x, y as a number. 
# For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
# Then generate a new list based on all combination of x and y.
# For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# And output will be [[0,0],[0,1]]

# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]


x = int(input("Enter x: "))
y = int(input("Enter y: "))

l1 = [[i, j] for i in range(x) for j in range(y)]

print(l1)


# 17.	 What is the difference between add and update methods in set? 

# 18.	What is the difference between append and extend methods in list? 
# 19.	What is the difference between pop and remove methods? 
# 20.	What is the difference between discard, pop, remove methods? 
# 21.	How to create empty set? 

s1 = {}
print(s1)

# 22.	Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.

s1 = {1,2,3,4}
s2 = {2,4,6,8,10}

print(s1|s2)
print(s1 &s2) #-> intersection
print(s1-s2) #-> set difference
print(s1 ^ s2) #-> symmetric diff (uncommon elements)


# 23.	Create l2 as a list and perform set operation on s1 with l1 

l2 = [10,20,30]
print(s1 | l2)
print(s1 & l2)
print(s1 - l2)
print(s1 ^ l2)


# 24.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  @ddmm. 
# For example name = SURESH and DOB = 05-05-1978 then password will be SURE@0505 

name = input("Enter name : ")
dob = input('Enter DOB(dd-mm-yy) : ')

password = name[0:4] + '@'+ dob[0:2] + dob[3:5]


print(password)


# 25.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  last 4 digits of DOB or year @yyyy. 
# For example name = SURESH and DOB = 05-05-1978 then password will be SURE@1978 

name = input("Enter name : ")
dob = input('Enter DOB(dd-mm-yyyy) : ')

password = name[0:4] + '@'+ dob[6:]


print(password)


# 26.	Create the format mentioned here.
# *
# * *
# * * *
# * * * *

for i in range(1,5):
    print('*' * i)

# 27.	Create the format as mentioned below:
# ****
# ***
# **
# *

for i in range(5,1, -1):
    print('*' * i)


# 28.	Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D

Str_val = "ABCD"
n = ''
for i in range(len(Str_val)):
    n = n +' ' + Str_val[i]
    print(n)



# 29.	Create the format mentioned below:
# A
# BB
# CCC
# DDDD

Str_val = "ABCD"
n = ''
for i in range(len(Str_val)):
    for j in range(i):



# 30.	Create the format mentioned below:
# 1
# 22
# 333
# 4444

# for i in range(1, 5):
#     print(str(i) * i)



# 31.	Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA

val = "ABCD"

rev = val[::-1]   # Reverse string → DCBA

for i in range(1, len(rev) + 1):
    print(rev[:i])

# 32.	Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU

# User may pass any string.

s = input("Enter a string: ")
rev = s[::-1]
for i in range(1, len(rev) + 1):
    print(rev[:i])


# 33.	Create a list of odd numbers from 1 to 10
# 1.	Using for loop

odd_list = []
for i in range(1, 11):
    if i % 2 != 0:
        odd_list.append(i)

print(odd_list)

# 2.	Using comprehensive list

odd_list = [i for i in range(1, 11) if i % 2 != 0]
print(odd_list)

# 34.	Create even number list using for loop from 200 to 250

even_list = []
for i in range(200, 251):
    if i % 2 == 0:
        even_list.append(i)

print(even_list)


# 35.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer

List2 = [2, 70, 'work', 'para', 2.5, [1,2,3], (1,2), {1,2},{1:'a', 2:'b'}, 3, 10, 302.5]

new_list2 = []
for x in List2:
    if isinstance(x, (int, float, str, list, tuple)):
        new_list2.append(x * 2)
    else:
        new_list2.append(x)   

print(new_list2)


# 36.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]

# Multiply each and every element from list2 by 2 and store the answer in list3

List2 = [2, 70, 'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3, 10, 302.5]

List3 = []

for x in List2:
    if isinstance(x, (int, float, str, list, tuple)):
        List3.append(x * 2)
    else:
        List3.append(x) 

print("List3:", List3)


# 36.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element from list2 by 2 and store the answer in list3

List2 = [2,70,'work', "para", 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
List3 = [(x,x*2) for x in List2 if type(x) not in (set, dict) ]  # TypeError: unsupported operand type(s) for *: 'set' and 'int'
print(List3)


    # 37.	Create a function to accept marks from user utilize exception concept to validate proper marks.

# --> function
# --> try
#         --> if 
# --> except
# --> func call


def ValidateMarks():
    try:
        marks = input("Enter marks: ")
        if float(marks) < 100 or float(marks) > 0:
            print("Correct marks - ", marks)
        
    except ValueError:
        print("Enter proper marks.")

ValidateMarks()


# 38.	Create a function to validate user first name/last name. User first name/last name should contain only characters.
#  No special characters, numbers, space in name 

first_name = input("Enter firstname: ")
last_name = input("Enter lastname: ")
# name = input("Enter name: ")

def ValidateName(first_name, last_name):
    if first_name.isalpha() and last_name.isalpha():
        return first_name + ' ' + last_name
    else:
        return "Enter proper name with just characters. (No special characters, numbers, space in name)"
    
print(ValidateName(first_name, last_name))
    

# 39.	Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space. 

phone_num = input("Enter phone number: ")

def ValidatePhoneNum(phone_num):
    if phone_num.isdigit() and len(phone_num) == 10:
        output = "Accepted."
    else:
        output = "Enter valid number.(No Special character, alphabets and space.)"
    return output

print(ValidatePhoneNum(phone_num))
    



# 40.	Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB. 
# And password must be First name 4 characters and year of birth.

name = input("Enter name : ")
dob = input("Enter DOB : ")

def GeneratePassword(name, dob):
    if name.isalpha() and dob.isdigit() and dob[2] == '-' and dob[5] == '-':
        password = name[0:4]+dob[6:]
        return password
    else:
        return "Enter proper name/dob(dd-mm-yyyy)."


print(GeneratePassword(name,dob))

# 41.	Create a empty dictionary and ask user to enter values as name, DOB, mobile number 
# add all the details in dictionary with customer number as 1 for first time. 
# If user try to enter another value, then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}

# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}


n = int(input("How many entries? "))
dict1 = {}

for i in range(1,n+1):
    name = input("Enter name : ")
    dob = input("Enter DOB : ")
    mobile = input("Enter mobile num: ")

    dict1[i] = dict({'name': name, 'DOB': dob, 'Mobile': mobile})

print(dict1)



## OR
dict1 = {}

for i in range (1,10):
    name = input("Enter name : ")
    dob = input("Enter DOB : ")
    mobile = input("Enter mobile num: ")

    if name.isalpha() and mobile.isdigit() and len(mobile) == 10:
        dict1[i] = dict({'name': name, 'DOB': dob, 'Mobile': mobile})
        print(dict1)
        if input("Want to enter more? (y/n): ").upper() != 'Y':
            break

        print()
    else:
        print("Enter the correct details.")
        break
        
print("Final dictionary",dict1)

# 45.	Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}

Dict1 = {"Key": {"subkey": 20},"k2": {"sub2": 5}, "k3": {"sub4": 16},"k4": {"sub4": 6}}

sorted_dict = dict(
    sorted(
        Dict1.items(),
        key=lambda item: list(item[1].values())[0]
    )
)

print(sorted_dict)

# 46.	Create a function to calculate age till now.
import datetime
from datetime import datetime

def calculate_age():

    dob_input = input("Enter DOB (dd-mm-yyyy): ")

    dob = datetime.strptime(dob_input, "%d-%m-%Y")
    today = datetime.today()

    age = today.year - dob.year

    # Check if birthday occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print("Your age is:", age)


calculate_age()

# 47.	Create a function to check age eligibility for given customer based on DOB. 
# Function will take two input DOB and ELIGIBILITY age.

from datetime import datetime
from datetime import date 

def check_eligibility(dob, eligibility_age):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
   
    if age >= eligibility_age:
        return f"Eligible (Age: {age})"
    else:
        return f"Not Eligible (Age: {age})"
 
print(check_eligibility(dob = date(2002, 3, 4), eligibility_age =18))

# 48.	Create a function to check if string is palindrome or not ? 
# For example, if input is NITIN then reverse of the string is same then it is palindrome. 
# If input is ANIL then reverse is LINA which is not same then it is not palindrome.  

s = input("Enter a string: ")
def Pallindrome(s):

    if s.upper() == s[::-1].upper():
        print("Its a pallindrome.")
    else:
        print("Not a pallindrome.")

Pallindrome(s)


# 49.	Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 …..  upto 100 
n = 100
def Fibonacci():
    a = 0
    b = 1
    for i in range(100):
        print(a, end= " ")
        a,b = b, a+b

Fibonacci()



# 50.	Write a code to generate factorial of the number  For example: factorial of 5 = 5! = 5*4*3*2*1
def factorial(n):
    fact = 1
    
    for i in range(1, n+1):
        fact *= i
        
    return fact

print(factorial(5))

# 51.	Write a program to find largest number in the list.

def LargestNum(lst):
    largest = lst[0]
    
    for num in lst:
        if num > largest:
            largest = num
            
    return largest

l = [10, 45, 2, 99, 23]
print(LargestNum(l))

# 52.	Write a program to check frequency of each element in the list.

l = [1,2,2,3,4,1,2,5]

def FreqCount(l):
    freq = {}
    
    for item in l:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
            
    return freq

print(FreqCount(l))

# 53.	There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] then write a program to find common elements in the list.

l1 = [1,2,3,4,5]
l2 = [3,2,8,7,9]

def CommonElements(l1, l2):
    common = []
    
    for item in l1:
        if item in l2 and item not in common:
            common.append(item)
            
    return common

print(CommonElements(l1, l2))

# Restaurant bill printing

# 57.	Build a function to print bill. Generate the bill as mentioned below. 
# With just string alignment

sr_num = input("Enter serial number: ")
menu = input("Enter the menu : ")
quantity = int(input("Enter the quatity: "))
price = int(input("Enter the price: "))

print("{:^50}".format("----------------------------------------------------"))
print("{:^50}".format(":Welcome to Shiv Sagar:"))
print("{:^50}".format("----------------------------------------------------"))

print("{:2} {:^8} {:^15} {:^20}".format('SrNo.','Menu', 'Quantity', 'Price'))
print("{0:2} {1:^14} {2:^8} {3:^27}".format(sr_num, menu, quantity, price))
print("\n")
print("{:^50}".format("----------------------------------------------------"))
print("Total amount: ", quantity*price)
print("{:^50}".format("----------------------------------------------------"))


# -----------------


# Restaurant Bill Printing using Functions


def get_input():
    sr_num = input("Enter serial number: ")
    menu = input("Enter the menu: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))
    return sr_num, menu, quantity, price


def calculate_total(qty, price):
    return qty * price


def print_bill(sr, menu, qty, price, total):

    print("{:^50}".format("----------------------------------------------"))
    print("{:^50}".format("Welcome to Shiv Sagar"))
    print("{:^50}".format("----------------------------------------------"))

    print("{:2} {:^8} {:^15} {:^20}".format(
        'SrNo.', 'Menu', 'Quantity', 'Price'
    ))

    print("{0:2} {1:^14} {2:^8} {3:^27}".format(
        sr, menu, qty, price
    ))

    print("\n")
    print("{:^50}".format("----------------------------------------------"))
    print("Total amount:", total)
    print("{:^50}".format("----------------------------------------------"))



sr, menu, qty, price = get_input()

total = calculate_total(qty, price)

print_bill(sr, menu, qty, price, total)


# ----------------


#Q. Print bill in file

sr_num = input("Enter serial number: ")
menu = input("Enter the menu : ")
quantity = int(input("Enter the quatity: "))
price = int(input("Enter the price: "))

bill_text = ""

bill_text += "{:^50}/n".format("----------------------------------------------------")
bill_text += "{:^50}/n".format(":Welcome to Shiv Sagar:")
bill_text += "{:^50}/n".format("----------------------------------------------------")

bill_text += "{:2} {:^8} {:^15} {:^20}/n".format('SrNo.','Menu', 'Quantity', 'Price')
bill_text += "{0:2} {1:^14} {2:^8} {3:^27}/n".format(sr_num, menu, quantity, price)
bill_text += "/n"

bill_text += "{:^50}/n".format("----------------------------------------------------")
bill_text += "Total amount: {}/n".format(quantity * price)
bill_text += "{:^50}/n".format("----------------------------------------------------")

print(bill_text)

bill = open("C:/Users/Rachana/Downloads/Bill-file.txt", 'w')
bill.write(bill_text)
bill.close()

