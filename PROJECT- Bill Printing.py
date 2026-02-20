# Bill printing project:-

import pyodbc
from datetime import datetime

try:
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-NVF0H8OV\\SQLEXPRESS;'
        'Database=RESTAURANT_DATA;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
except Exception as e:
    print("Database connection error:", e)
    exit()


class Restaurant:

    def ShowMenu(self):
        try:
            print("\n------ MENU ------")
            cursor.execute("SELECT * FROM Menu")
            for row in cursor:
                print(row.id, row.name, row.price)
            print("------------------")
        except Exception as e:
            print("Error fetching menu:", e)


    def NewOrderID(self):
        try:
            cursor.execute("SELECT ISNULL(MAX(order_id),1000)+1 FROM Order01")
            return cursor.fetchone()[0]
        except Exception as e:
            print("Error generating order id:", e)
            return None


    def PlaceOrder(self):
        try:
            table_no = int(input("Enter Table No: "))
        except ValueError:
            print("Invalid table number! ")
            print("\n Pls enter the correct table number.")
            return

        order_id = self.NewOrderID()
        if order_id is None:
            return

        order_time = datetime.now()

        while True:
            self.ShowMenu()

            item = input("Enter item name: ")

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity!")
                continue

            try:
                cursor.execute("SELECT id, price FROM Menu WHERE name=?",item)
                data = cursor.fetchone()

                if data is None:
                    print("Item not found")
                    continue

                menu_id, price = data
                total = price * quantity

                cursor.execute("""
                    INSERT INTO Order01
                    (order_id, table_no, menu_id,
                     price, quantity, total_amount,
                     order_datetime)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                order_id,
                table_no,
                menu_id,
                price,
                quantity,
                total,
                order_time)

                conn.commit()

            except Exception as e:
                print("Error placing order:", e)
                return

            # ch = input("Add more items? (yes/no): ").lower()
            # if ch != "yes":
            #     break

            while True:
                ch = input("Add more items? (yes/no): ").lower()

                if ch == "yes":
                    break     
                elif ch == "no":
                    print(f"\nOrder {order_id} placed for Table {table_no}")
                    return     
                else:
                    print("Invalid input! Please enter only 'yes' or 'no'.")



    def OrderIDForBill(self):
        try:
            table_no = int(input("Enter Table No: "))
        except ValueError:
            print("Invalid table number!")
            return None

        try:
            cursor.execute("""
                SELECT DISTINCT order_id, order_datetime
                FROM Order01
                WHERE table_no = ?
            """, table_no)

            orders = cursor.fetchall()

            if not orders:
                print("No orders for this table")
                return None

            print("\nAvailable Orders:")
            for o in orders:
                print("Order ID:", o[0], "| DateTime:", o[1])

            oid = int(input("Enter Order ID to print: "))
            return oid

        except Exception as e:
            print("Error fetching orders:", e)
            return None


    def PrintBill(self):
        oid = self.OrderIDForBill()
        if oid is None:
            return

        try:
            cursor.execute("""
                SELECT m.name,
                       o.price,
                       o.quantity,
                       o.total_amount,
                       o.order_datetime
                FROM Order01 o
                JOIN Menu m
                ON o.menu_id = m.id
                WHERE o.order_id = ?
            """, oid)

            data = cursor.fetchall()

            if not data:
                print("Invalid Order ID")
                return

            grand_total = 0
            order_time = data[0][4]   # datetime

            bill_text = "\n=========== SHIV SAGAR ===========\n"
            bill_text += f"Order ID : {oid}\n"
            bill_text += f"Date & Time : {order_time}\n"
            bill_text += "----------------------------------\n"
            bill_text += f"{'Item':<12}{'Qty':<6}{'Price':<8}{'Total':<8}\n"
            bill_text += "----------------------------------\n"

            for row in data:
                name, price, quantity, total, _ = row
                bill_text += f"{name:<12}{quantity:<6}{price:<8}{total:<8}\n"
                grand_total += total

            bill_text += "----------------------------------\n"
            bill_text += f"{'Grand Total':<26}{grand_total}\n"
            bill_text += "==================================\n"

            print(bill_text)

            ch = input("Print in file? (yes/no): ").lower()
            if ch == "yes":
                filename = f"Bill_{oid}.txt"
                with open(filename, "w") as f:
                    f.write(bill_text)
                print("Bill saved as", filename)

        except Exception as e:
            print("Error printing bill:", e)


r = Restaurant()

while True:
    print("""
1 Show Menu
2 Place Order
3 Print Bill
4 Exit
""")

    ch = input("Choice: ")

    if ch == "1":
        r.ShowMenu()
    elif ch == "2":
        r.PlaceOrder()
    elif ch == "3":
        r.PrintBill()
    elif ch == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice")
