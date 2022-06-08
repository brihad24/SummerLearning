# To start a car and stop with commands and  exit  the program
status = ""

while True:
    action = input("> ").lower()

    if action == "help":
        print("start - to start the car" + "\n" + "stop - to stop the car" + "\n" + "quit - to quit the game")
    
    elif action == "start" and status != "started":
        print("Car started, ready to go!")
        status = "started"

    elif action == "start" and status == "started":
        print("Car is already started and ready to go!")
    
    elif action == "stop" and status == "started":
        print("Car has stopped")
        status = "stopped"

    elif action == "stop" and status != "started":
        print("Car has not been started")

    elif action == "quit":
        break
    
    else:
        print("I dont understand that, refer to 'help' to check list of commands")