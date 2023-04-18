import ElevHandler


looping = True


skola = ElevHandler.ElevHandler()

skola.print_meny()

while looping:
    val = skola.print_meny()
    print("hej")

    if (val == "1"):
        print("lista elever")
    elif (val == "2"):
        print("add elev")
    elif (val == "3"):
        print("tabort elev")

    elif (val == "4"):
        break