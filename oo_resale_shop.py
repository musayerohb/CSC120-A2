from computer import *

class ResaleShop:

    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # What methods will you need?
    
    inventory = []
    name = ""
    
    def add_to_inventory(self, computer) -> None:
        """"Adds a created computer to the inventory, which is a list.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :return: None
        """
        self.inventory.append(computer)
    
    def remove_from_inventory(self, computer) -> None:
        """Removes a created computer from the inventory, which is a list.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :return: None"""
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Error, computer not found in inventory.")

    def update_price(self, computer, new_price) -> None:
        """"Updates the price of a selected computer.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :param new_price: (int) The new price you want to give the selected computer.
        :return: None"""
        if computer in self.inventory:
            computer.price = new_price
        else:
            print("Sorry! This computer is not in the inventory.")
    
    def update_operating_system(self, computer, new_OS) -> None:
        """"Updates the operating system of a selected computer.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :param new_OS: (str) The new operating system you want to install on the computer.
        :return: None"""
        if computer in self.inventory:
            computer.operating_system = new_OS #why is operating_system not working?
        else: 
            print("Sorry! Computer not found in inventory.")
    
    def refurbish(self, computer, new_OS) -> None:
        """Changes the price of a selected computer based on the year it was made in and updates its OS. 

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :param new_OS: (str) The new operating system you want to install on the computer.
        :return: None"""
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_OS is not None:
                computer.operating_system = new_OS # update details after installing new OS
        else:
            print("Item not found. Please select another item to refurbish.")

    def __init__(self, name, inventory) -> None:
        """"Adds a created computer to the inventory, which is a list.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :return: None
        """
        self.name = name
        self.inventory = inventory
        

