import pandas as pd


class Order:
    def __init__(self, date, day, table_num, bill_num):
        self.date = date
        self.day = day
        self.table_num = table_num
        self.bill_num = bill_num
        self.final_order = []
        self.amount = []
        self.total_amount = ""
        self.GST = ""
        self.total_bill = ""

    def add_item(self, name, price, quantity):
        current_item = (name, price, quantity)
        self.final_order.append(current_item)

    def calculate_bill(self):
        bill = []
        for i in self.final_order:
            amount = i[1] * i[2]
            bill.append(amount)
        total_amount = sum(bill)
        GST = (total_amount * 5) / 100
        total_bill = total_amount + GST
        self.amount = bill
        self.total_amount = total_amount
        self.GST = GST
        self.total_bill = total_bill

    def print_bill(self):
        print(f"date:{self.date},       day:{self.day}")
        print(f"table_num:{self.table_num},     bill_num:{self.bill_num}")
        print(f"final_order:{self.final_order}")
        df = pd.DataFrame(self.final_order, columns=["item", "quantity", "price"])
        df["Amount"] = self.amount
        print("final_bill:\n", df, "\n")
        print(f"your amount is:{self.total_amount}")
        print(f"5 % GST is:{self.GST}")
        print(f"total_bill_is:{self.total_bill}")


# if __name__ == "__main__":
#     O1 = Order("03/11/2023", "Saturday", 3, 12)
#     O1.add_item("chicken tandoor", 350, 3)
#     # O1.calculate_bill()
#     print(O1.print_bill())
#     #     O1.add_item("sandwich", 2, 90)
#     #     O1.add_item("dessart", 4, 90)
