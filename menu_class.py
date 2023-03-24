import pandas as pd

# The global variables get defined outside any function- usually at the very top of a program
# Reusing names in and out of function will be referred as "showing names" in Pycharm therefore
# causes "shadows name from outer scope" it just warning doesnt make your code unable to run.
#
file_path = "C:/Users/admin/Desktop/Cafe_Menu_card.xlsx"

class Menu:
    def __init__(self, file_path):
        menu_df = pd.read_excel(file_path)
        self.menu_df = menu_df

    def get_item(self, item_no):
        item = self.menu_df.loc[item_no]
        name = item["Item_Name"]
        price = item["Rate"]
        return name, price


# if __name__ == "__main__":
#     M1 = Menu(file_path)
#     item = M1.get_item(4)
#     print(item)
