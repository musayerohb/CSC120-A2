class Computer:
    # What attributes will it need?
    # How will you set up your constructor?
    # What methods will you need?
    # Remember: in python, all constructors have the same name (__init__)

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        """Creates a computer object.
        :param self: The computer itself.
        :param description: (str) The description of the computer.
        :param processor_type: (str) The computer's processor type.
        :param hard_drive_capacity: (int) The computer's hard drive capacity.
        :param memory: (int) The computer's memory.
        :param operating_system: (str) The computer's OS.
        :param year_made: (int) The year in which the computer was made.
        :param price: (int) The price of computer. 


        """
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    

    def printDetails(self) -> None:
        """Prints out the details of the created computer.
        :param self: The constructed computer.
        :return: None
        
        """
        print("price:", self.price)
        print("description:", self.description)
        print("Processor type:", self.processor_type)
        print("hard drive capacity:", self.hard_drive_capacity)
        print("memory:", self.memory)
        print("operating system:", self.operating_system)
        print("year made:", self.year_made)
    
    def update_price(self, new_price) -> None:
        """"Updates the price of a selected computer.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :param new_price: The new price you want to give the selected computer.
        :return: None
        """
        self.price = new_price
        
    def update_operating_system(self, new_OS) -> None:
        """"Updates the operating system of a selected computer.

        :param self: The ResaleShop.
        :param computer: The selected computer.
        :param new_OS: The new operating system you want to install on the computer.
        :return: None
        """
        self.operating_system = new_OS


