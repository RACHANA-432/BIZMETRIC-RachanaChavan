# College Fees - Project
import pyodbc
from datetime import datetime

class CollegeFee:

    L1 = ["HR", "FINANCE", "MARKETING", "DS"]
    BASE_FEE = 200000
    HOSTEL_FEE = 200000
    FOOD_PER_MONTH = 2000
    TRANSPORT_PER_SEM = 13000

    def __init__(self, name, subject, analytics, hostel, food_months, transport):
        self.name = name
        self.subject = subject
        self.analytics = analytics
        self.hostel = hostel
        self.food_months = food_months
        self.transport = transport
        self.course_fee = 0
        self.total_fee = 0
        self.student_id = None

        self.analytics_fee = 0
        self.hostel_fee = 0
        self.food_fee = 0
        self.transport_fee = 0
        self.total_fee = 0

    def calculate_fee(self):

        self.course_fee = CollegeFee.BASE_FEE

        if self.subject in ["HR", "MARKETING"] and self.analytics == "Y":
            self.analytics_fee = CollegeFee.BASE_FEE * 0.10
        else:
            self.analytics_fee = 0

        if self.hostel == "Y":
            self.hostel_fee = CollegeFee.HOSTEL_FEE
        else:
            self.hostel_fee = 0

        self.food_fee = self.food_months * CollegeFee.FOOD_PER_MONTH

        if self.transport == "semester":
            self.transport_fee = CollegeFee.TRANSPORT_PER_SEM
        elif self.transport == "annual":
            self.transport_fee = CollegeFee.TRANSPORT_PER_SEM * 2

        self.total_fee = (
            self.course_fee
            + self.analytics_fee
            + self.hostel_fee
            + self.food_fee
            + self.transport_fee
        )

    def save_to_db(self):
        try:
            conn = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=LAPTOP-NVF0H8OV\\SQLEXPRESS;"
                "Database=COLLEGE_DATA;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO CollegeFeeDetails
                (Name, Subject, Analytics, Hostel, FoodMonths,
                 TransportType, CourseFee, TotalFee)
                OUTPUT INSERTED.StudentID
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.name,
                self.subject,
                self.analytics,
                self.hostel,
                self.food_months,
                self.transport,
                int(self.course_fee),
                int(self.total_fee)
            ))

            self.student_id = cursor.fetchone()[0]
            conn.commit()
            conn.close()
            print("Data saved successfully!")

        except Exception as e:
            print("Database Error:", e)

    def generate_Receipt(self):

        choice = input("Do you want to print the Receipt? (Y/N): ").upper()
        if choice == "Y":
            filename = f"{self.student_id}_{self.name.replace(' ', '_')}.txt"
            now = datetime.now()
            current_date = now.strftime("%d-%m-%Y")
            current_time = now.strftime("%I:%M:%S %p")

            with open(filename, "w", encoding="utf-8") as file:
                file.write("====== COLLEGE FEE Receipt ======\n\n")

                file.write(f"Date         : {current_date}\n")
                file.write(f"Time         : {current_time}\n\n")

                file.write(f"Student ID   : {self.student_id}\n")
                file.write(f"Name         : {self.name}\n")

                file.write("\n------ FEE BREAKDOWN ------\n\n")
                file.write(f"Base Fee             : Rs. {CollegeFee.BASE_FEE}\n")
                file.write(f"Analytics Fee (10%)  : Rs. {int(self.analytics_fee)}\n")
                file.write(f"Hostel Fee           : Rs. {self.hostel_fee}\n")
                file.write(f"Food Fee             : Rs. {self.food_fee}\n")
                file.write(f"Transport Fee        : Rs. {self.transport_fee}\n")

                file.write("\n--------------------------------\n")
                file.write(f"TOTAL ANNUAL COST    : Rs. {int(self.total_fee)}\n")
                file.write("--------------------------------\n")

            print("Receipt generated:", filename)

        else:
            print("Receipt not generated.")


name = input("Enter Student Name: ").strip()

print("\nAvailable Courses:")
for course in CollegeFee.L1:
    print("-", course)

while True:
    subject = input("Enter subject: ").strip().upper()
    if subject in CollegeFee.L1:
        break
    else:
        print("Invalid Subject!")

analytics = "N"
if subject in ["HR", "MARKETING"]:
    while True:
        analytics = input("Analytics (Y/N): ").strip().upper()
        if analytics in ["Y", "N"]:
            break
        else:
            print("Enter Y or N")
else:
    print("Analytics not available for this subject.")

while True:
    hostel = input("Hostel (Y/N): ").strip().upper()
    if hostel in ["Y", "N"]:
        break
    else:
        print("Enter Y or N")

while True:
    try:
        food_months = int(input("Food (How many months?): "))
        if food_months >= 0:
            break
    except:
        print("Enter valid number")

while True:
    transport = input("Transportation (semester/annual): ").strip().lower()
    if transport in ["semester", "annual"]:
        break
    else:
        print("Enter semester or annual")

student = CollegeFee(name, subject, analytics, hostel, food_months, transport)

student.calculate_fee()
student.save_to_db()
student.generate_Receipt()