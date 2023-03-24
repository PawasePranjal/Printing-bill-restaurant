from menu_class import Menu
from order_class import Order

date_formate = "%m/%d/%Y"

file_path = "C:/Users/admin/Desktop/Cafe_Menu_card.xlsx"
M1 = Menu(file_path)
get_item = M1.get_item(3)

O1 = Order("3/23/2023", "Thursday", 3, 11)
O1.add_item(*M1.get_item(3), 2)
O1.add_item(*M1.get_item(4), 3)

O1.calculate_bill()
print(O1.print_bill())
