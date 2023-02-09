import computer
import oo_resale_shop 

# this is just for testing my code. personal use.

def main():
    Mycomputer = computer.Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
    Mycomputer.printDetails()
    Mycomputer.update_price(100)
    print(Mycomputer.price)
    Mycomputer.update_operating_system("toot toot 13")
    print(Mycomputer.operating_system)

    new_computer = computer.Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
    Mystore = oo_resale_shop.ResaleShop("Musa's Computer Rendezvous", [])
    Mystore.add_to_inventory(new_computer)
    print(Mystore.inventory)
    Mystore.remove_from_inventory(new_computer)
    print(Mystore.inventory)
    print('')

    Mystore.add_to_inventory(new_computer)
    Mystore.update_price(new_computer, 200)
    print(new_computer.price)
    Mystore.update_operating_system(new_computer, "fuji apple xp")
    print(new_computer.operating_system)
    Mystore.refurbish(new_computer, "unicorn blaster 7")
    print(new_computer.price)
    print(new_computer.operating_system)

main()
