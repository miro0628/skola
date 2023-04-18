import Elev

class ElevHandler:
    
    
    #constructor
    def __init__(self):
        self.ElevList = []
    def print_meny(self):
        print("----------------------------------------")
        print("\t\t\tMENY")
        print("\t\t\t1. Lista elever")
        print("\t\t\t2. Lägg till elever")
        print("\t\t\t3. Tabort elev")
        print("\t\t\t4. Spara och avsluta")
        print("----------------------------------------")

        val = input("Gör ditt val: ")

        return val
    def add_elev(self, elevnamn, utbildning, id):
        id_elev = Elev.Elev(elevnamn, utbildning, id)
        self.ElevList.append(id_elev)