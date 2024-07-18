from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_today = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    choice = input(f"Choose your drink? {menu_today.get_items()} : ")
    if(choice == "off"):
        break
    elif (choice == "report"):
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu_today.find_drink(order_name=choice)
        if ( coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost)):
            coffee_maker.make_coffee(item)
