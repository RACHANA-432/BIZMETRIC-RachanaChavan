# Bill printing project

import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NVF0H8OV\\SQLEXPRESS;'
    'Database=RESTAURANT_DATA;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()


class Restaurant:
    def ShowMenu(self):
        print("\n------ MENU ------")
        cursor.execute("SELECT * FROM Menu")
        for row in cursor:
            print(row.id, row.name, row.price)

        print("------------------")


    def NewOrderID(self): 
        cursor.execute(
            "SELECT ISNULL(MAX(order_id),1000)+1 FROM Order01"
        )
        return cursor.fetchone()[0]


    def PlaceOrder(self):
        table_no = int(input("Enter Table No: "))
        order_id = self.NewOrderID()

        while True:
            self.ShowMenu()
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            cursor.execute(
                "SELECT id, price FROM Menu WHERE name=?",
                item
            )
            data = cursor.fetchone()

            if data is None:
                print("Item not found")
                continue

            menu_id, price = data
            total = price * quantity
            cursor.execute("""
                INSERT INTO Order01
                (order_id, table_no, menu_id,
                 price, quantity, total_amount)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            order_id,
            table_no,
            menu_id,
            price,
            quantity,
            total)

            conn.commit()

            ch = input(
                "Add more items? (yes/no): "
            ).lower()

            if ch != "yes":
                break

        print(f"\nOrder {order_id} placed for Table {table_no}")


    def OrderIDForBill(self):
        table_no = int(input("Enter Table No: "))
        cursor.execute("""
            SELECT DISTINCT order_id
            FROM Order01
            WHERE table_no = ?
        """, table_no)
        orders = cursor.fetchall()

        if not orders:
            print("No orders for this table")
            return None
        
        print("\nAvailable Orders:")
        for o in orders:
            print("Order ID:", o[0])

        oid = int(input("Enter Order ID to print: "))
        return oid


    def PrintBill(self):
        oid = self.OrderIDForBill()
        if oid is None:
            return

        cursor.execute("""
            SELECT m.name,
                   o.price,
                   o.quantity,
                   o.total_amount
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

        bill_text = "\n------ SHIV SAGAR ------\n"
        bill_text += f"Order ID: {oid}\n"
        bill_text += "-------------------------\n"

        for row in data:
            name, price, quantity, total = row
            bill_text += (f"{name} x{quantity} = {total}\n")
            grand_total += total

        bill_text += "-------------------------\n"
        bill_text += f"Grand Total: {grand_total}\n"
        print(bill_text)


        ch = input("Print in file? (yes/no): ").lower()

        if ch == "yes":
            filename = f"Bill_{oid}.txt"
            with open(filename, "w") as f:
                f.write(bill_text)
            print("Bill saved as", filename)


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