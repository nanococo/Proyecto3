import socket, os, pickle

def printIterable(iterable):
    for i in iterable:
        print(i)


def countryQuerySection(s):
    codeList = ["03"]
    s.send(pickle.dumps(codeList))
    countryList = pickle.loads(s.recv(8192))

    os.system("cls")
    print("These are the found countries: ")
    printIterable(countryList)
    input("Press enter to continue...")


def cityQuerySection(s):
    codeList = ["03"]
    s.send(pickle.dumps(codeList))
    countryList = pickle.loads(s.recv(8192))

    end = False
    mistake = False
    while not end:
        os.system("cls")
        print("These are the found countries: ")
        printIterable(countryList)
        print(str(len(countryList) + 1) + ") Return")
        if mistake:
            print("This is not an option. Please select a given option")
            mistake = False
        print("Please, choose a country to find associated cities.")
        try:
            op = int(input("Enter an option: "))

            if op == len(countryList) + 1:
                end = True
            else:
                codeList = ["04", op]
                s.send(pickle.dumps(codeList))
                cityList = pickle.loads(s.recv(8192))

                if not cityList:
                    print("No cities found for given country")
                    input("Press enter to continue...")
                else:
                    print("Found cities:")
                    printIterable(cityList)
                    input("Press enter to continue...")

        except ValueError:
            mistake = True

def connectionQuerySection(s):
    end = False
    while not end:
        os.system('cls')
        print("Query a connection. To exit; please type 0.")
        country = input("PLease Type a Country (code): ")
        if country != "0":
            city = input("Please typ a City (code): ")
            if city != "0":
                codeList = ["05", country, city]
                s.send(pickle.dumps(codeList))
                connectionList = pickle.loads(s.recv(8192))

                if not connectionList:
                    print("Not found connections with given parameters. Press enter to re-try.")
                    input("Press enter to continue...")
                else:
                    print("Found connections:")
                    printIterable(connectionList)
                    input("Press enter to continue...")
                    end = True
            else:
                end = True
        else:
            end = True

def trainQuerySection(s):
    end = False
    while not end:
        os.system("cls")
        print("Please enter a train type (01,02,03,04). Or type 0 to return")
        train = input()

        codeList = ["06", train]
        s.send(pickle.dumps(codeList))
        trainList = pickle.loads(s.recv(8192))

        if not trainList:
            print("Not found trains with given parameters. Press enter to re-try.")
            input("Press enter to continue...")
        else:
            print("Found trains:")
            printIterable(trainList)
            input("Press enter to continue...")
            end = True

def pricesQuerySection(s):
    end = False
    while not end:
        os.system("cls")
        print("Please type a train (code) to check its routes prices. Or type 0 to return")
        train = input()

        codeList = ["07", train]
        s.send(pickle.dumps(codeList))
        prices = pickle.loads(s.recv(8192))

        if not prices:
            print("Not found prices with given parameters. Press enter to re-try.")
            input("Press enter to continue...")
        else:
            print("Found prices:")
            printIterable(prices)
            input("Press enter to continue...")
            end = True

def seatsQuerySection(s):
    end = False
    while not end:
        os.system("cls")
        print("Please type a train (code) to check its seats. Or type 0 to return")
        train = input()

        codeList = ["08", train]
        s.send(pickle.dumps(codeList))
        seats = pickle.loads(s.recv(8192))

        if not seats:
            print("Not found seats with given parameters. Press enter to re-try.")
            input("Press enter to continue...")
        else:
            print("Found seats:")
            printIterable(seats)
            input("Press enter to continue...")
            end = True

def routesQuerySection(s):
    end = False
    while not end:
        os.system("cls")
        print("Please type a city (code) to check its routes. Or type 0 to return")
        city = input()

        codeList = ["09", city]
        s.send(pickle.dumps(codeList))
        routes = pickle.loads(s.recv(8192))

        if not routes:
            print("Not found routes with given parameters. Press enter to re-try.")
            input("Press enter to continue...")
        else:
            print("Found routes:")
            printIterable(routes)
            input("Press enter to continue...")
            end = True


def customRoutes(s):
    reservations = []
    end = False
    while not end:
        os.system("cls")
        print("Welcome. Please type your depart country and city and your arrival country and city. The system will attempt to search and "
              "create a route for your based on existent connections offered by the system. Also, search for cheapest or fastest")

        depCountry = input("Departure Country: ")
        depCity = input("Departure City: ")
        arrCountry = input("Arrival Country: ")
        arrCity = input("Arrival City: ")

        codeList = ["41", "", depCountry, depCity, arrCountry, arrCity]
        s.send(pickle.dumps(codeList))
        routes = pickle.loads(s.recv(8192))


        print(routes)
        if not routes:
            print("Not found seats with given parameters. Press enter to re-try.")
            end = True
            input("Press enter to continue...")
        else:
            print("Found routes:")

            for i in routes:
                print("\n")
                count = 0
                print("Optional Route:")
                for j in range(len(i)):
                    if j==len(i)-1:
                        print("Total duration: "+str(i[j]))
                    else:
                        count+=1
                        print(str(count) + ") Train Type: " + i[j][0] +". Train Code: " + i[j][1] +". Train Name: " + i[j][2] + ". Capacity: " + i[j][3] +". Goes from " + i[j][6][0] + ", " +i[j][6][1] + " to " + i[j][6][2] + ", " +i[j][6][3] +". Cost: " + i[j][6][4])
                        # userOp = input("Would you like to reserve seats with this route? (Y/N)")
                        # if userOp == "Y" or userOp == "y":
                        #     try:
                        #         for i in routes:
                        #             print("Train: " + i[2] + ". Available seats: " + i[6][4] + ". Price per seat: " + i[3])
                        #         print("Please state how many seats you would like to reserve")
                        #         seatsToReserve = int(input("# of Seats to reserve: "))
                        #         price = 0
                        #         for i in routes:
                        #             selectedList = [i[0], i[1], i[2], i[6][0], i[6][1], i[6][2], i[6][3], i[3], i[6][4]]
                        #             if int(i[6][4]) < seatsToReserve:
                        #                 print("Not enough seats to reserve. Try again")
                        #                 input("Press enter...")
                        #                 end = True
                        #                 break
                        #             else:
                        #                 price += (int(i[3]) * seatsToReserve)
                        #                 price2 = (int(i[3]) * seatsToReserve)
                        #                 selectedList.append(seatsToReserve)
                        #                 selectedList.append(price2)
                        #                 reservations += [selectedList]
                        #         print(reservations)
                        #         print("Total Cost: " + str(price))
                        #         input("Press enter...")
                        #         end = True
                        #         return reservations
                        #     except ValueError:
                        #         print("Error with provided values. Please try again")
                        #         input("Press enter to continue...")
                        #         return []
                        # else:
                        #     return []



def reservationQuerySection(s):
    end = False
    reservations = []
    while not end:
        os.system("cls")
        # ------------ This sections queries a city and a country for the route ---------------

        print("Please select one option")
        print("1) Fixed routes")
        print("2) Custom routes")
        print("Press anything else to return...")
        op1 = input("Option: ")

        if op1 == "1":
            print("Welcome to reservation. Please, type a departure country (code) and city (code) to start. Type 0 to return")
            selectedCountry = input("Country: ")
            selectedCity = input("City: ")

            if selectedCity == "0" or selectedCountry == "0":
                end = True
                break

            codeList = ["10", selectedCountry, selectedCity]
            s.send(pickle.dumps(codeList))
            tempList = pickle.loads(s.recv(8192))


            if not tempList:
                # If not found, goes to start again
                print("Not found connections with given parameters. Press enter to re-try.")
                input("Press enter...")
                end = True
            else:

                # ------------------------------- End Section 1 ----------------------------------------
                # --------------------------- Selecting Seat number section -----------------------------
                count = 0
                for i in tempList:
                    count += 1
                    print(str(count) + ") Train Type: " + i[0] +
                          ". Train Code: " + i[1] +
                          ". Train Name: " + i[2] +
                          ". Goes from " + i[3] + ", " +
                          i[4] + " to " + i[5] + ", " +
                          i[6] +
                          ". Capacity: " + i[7] +
                          ". Cost: " + i[8])
                while not end:
                    print("Please select one route. Type 0 to return.")
                    try:
                        route = int(input()) - 1
                        if route == -1:
                            end = True
                            break
                        selectedList = tempList[route]

                        print("Available seats: " + selectedList[7] + ". Price per seat: " + selectedList[8])
                        print("Please state how many seats you would like to reserve")
                        seatsToReserve = int(input("# of Seats to reserve: "))

                        if int(selectedList[7]) < seatsToReserve:
                            print("Not enough seats to reserve. Try again")
                            input("Press enter...")
                            end = True
                        else:
                            price = int(selectedList[8]) * seatsToReserve
                            print("Total Cost: " + str(price))
                            input("Press enter...")
                            selectedList.append(seatsToReserve)
                            selectedList.append(price)
                            print(selectedList)
                            reservations += [selectedList]
                            end = True
                    except ValueError:
                        print("Error with provided values. Please try again")
        elif op1 == "2":
            reservations += customRoutes(s)
        else:
            return reservations

def billing(s, reservations, userName):
    # reservations = [['01', 'TG6K8', 'BALAZO', 'GR', 'ARH', 'NO', 'BGO', '1500', '963', 3, 2889]]
    count = 0
    end = False
    error = False
    while not end:
        os.system("cls")

        if reservations:
            if error:
                print("This was not an option. Please try again")

            for i in range(len(reservations)):
                print("Ticket: " + str(count + 1) + ") Train Type: " + str(reservations[i][0]) + ". Train Code: " + str(
                    reservations[i][1]) + ". Train name: " + str(reservations[i][2]) + ". Goes from: " + str(
                    reservations[i][3]) + ", " + str(reservations[i][4]) + " to " + str(
                    reservations[i][5]) + ", " + str(
                    reservations[i][6]) + ". Seats to reserve: " + str(reservations[i][9]) + ". Price: " + str(
                    reservations[i][10]))

            print("Is this OK with you? Y/N")
            op = input()

            if op == "Y" or op == "y":

                codeList = ["11", reservations, userName]
                s.send(pickle.dumps(codeList))
                confirmation = pickle.loads(s.recv(8192))

                if confirmation:
                    reservations = []
                    print("Billing successful")
                    input("Press enter to continue...")
                    end = True
                else:
                    print("Billing successful. Please try again.")
                    end = True
                    break
            elif op == "N" or op == "n":
                print("Delete reservations? Y/N")
                op2 = input()

                if op2 == "Y" or op2 == "y":
                    reservations = []
                    end = True
                else:
                    end = True
            else:
                error = True
        else:
            print("No reservations found.")
            input("Press enter to return...")
            end = True

def inserts(s):
    end = False
    while not end:
        os.system("cls")
        print("Please select an option to insert")
        print("1) Insert Country")
        print("2) Insert City")
        print("3) Insert Connection")
        print("4) Insert Route")
        print("5) Insert Train")
        print("6) Exit")

        op = input("Option: ")

        if op == "1":
            os.system("cls")
            print("Please type a city code and a name to insert")
            newCountryCode = input("Country Code: ")
            newCountryName = input("Country Name: ")

            codeList = ["14", newCountryCode, newCountryName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Country is already present. Press enter to re-try.")
                input("Press enter to continue...")
            else:
                print("Successfully inserted:")
                input("Press enter to continue...")
                end = True


        elif op == "2":
            os.system("cls")
            print("Please type a country code for the city, the city and its name.")
            countryCodeForCity = input("Country code: ")
            newCityCode = input("City code: ")
            newCityName = input("City name: ")

            codeList = ["15", countryCodeForCity, newCityCode, newCityName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("City is already present. Press enter to re-try.")
                input("Press enter to continue...")
            else:
                print("Successfully inserted:")
                input("Press enter to continue...")
                end = True


        elif op == "3":

            os.system("cls")
            intCorrect = False
            newConnDuration = ""
            print("Please type a depart country and city, a connection code, an arrival country and city, and the duration")
            newConnDepCountry = input("Depart Country (code): ")
            newConnDepCity = input("Depart City (code): ")
            newConnCode = input("Connection code: ")
            newConnArrCountry = input("Arrival Country (code): ")
            newConnArrCity = input("Arrival city (code): ")
            while not intCorrect:
                try:
                    newConnDuration = int(input("Duration (numbers): "))
                    intCorrect = True
                    newConnDuration = str(newConnDuration)
                except ValueError:
                    print("Error, please type an int")

            codeList = ["16", newConnDepCountry, newConnDepCity, newConnCode, newConnArrCountry, newConnArrCity, newConnDuration]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Connection is already present. Press enter to re-try.")
                input("Press enter to continue...")
            else:
                print("Successfully inserted:")
                input("Press enter to continue...")
                end = True



        elif op == "4":
            # THIS IS THE ROUTE SECTION
            os.system("cls")
            correctInt = False
            print("Please enter a type of train, a train code to assign the route to, a depart country and city, an arrival country and city and a price")
            newRouteTrainType = input("Train type: ")
            newRouteTrainCode = input("Train code: ")
            newRouteDepartCountry = input("Depart country (code): ")
            newRouteDepartCity = input("Depart City (code): ")
            newRouteArrivalCountry = input("Arrival Country (code): ")
            newRouteArrivalCity = input("Arrival City (code): ")
            newRoutePrice = ""

            while not correctInt:
                try:
                    newRoutePrice = int(input("Price: "))
                    correctInt = True
                    newRoutePrice = str(newRoutePrice)
                except ValueError:
                    print("Please use integers")

            codeList = ["17", newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Route is already present. Press enter to re-try.")
                input("Press enter to continue...")
            else:
                print("Successfully inserted:")
                input("Press enter to continue...")
                end = True


        elif op == "5":
            correctInt = False
            os.system("cls")
            print("Please type a train type, a train code, a train name, the seats and the origin country and city")
            newTrainType = input("Train type (1,2,3,4): ")
            newTrainCode = input("Train code: ")
            newTrainName = input("Train name: ")
            newTrainSeats = ""
            while not correctInt:
                try:
                    newTrainSeats = int(input("Seats: "))
                    correctInt = True
                    newTrainSeats = str(newTrainSeats)
                except ValueError:
                    print("Please use integers")

            newTrainCountry = input("Country (code): ")
            newTrainCity = input("City (code): ")

            codeList = ["18", newTrainType, newTrainCode, newTrainName, newTrainSeats, newTrainCountry, newTrainCity]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Train is already present. Press enter to re-try.")
                input("Press enter to continue...")
            else:
                print("Successfully inserted:")
                input("Press enter to continue...")
                end = True


        elif op == "6":
            end = True

def deletes(s):
    end = False
    while not end:
        os.system("cls")
        print("Welcome to delete menu. Please, choose an option")
        print("1) Delete country")
        print("2) Delete city")
        print("3) Delete connection")
        print("4) Delete route")
        print("5) Delete train")
        print("6) Return")
        op = input()

        if op == "1":
            # THIS DELETES COUNTRY
            print("Please, type a country code to delete.")
            print("WARNING: THIS WILL DELETE ALL ENTRIES RELATED TO THE COUNTRY. PROCEED WITH CAUTION")
            countryToDel = input("Country (code): ")

            codeList = ["19", countryToDel]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not delete.")
                input("Press enter to continue...")
            else:
                print("Successfully deleted:")
                input("Press enter to continue...")
                end = True


        elif op == "2":
            # THIS DELETES CITIES
            print("Please type a country code and the city code you will delete.")
            print("WARNING: THIS WILL DELETE ALL ENTRIES RELATED TO THE CITY. PROCEED WITH CAUTION")
            countryCode = input("Country (code): ")
            cityToDelete = input("City to delete (code): ")

            codeList = ["20", countryCode, cityToDelete]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not delete.")
                input("Press enter to continue...")
            else:
                print("Successfully deleted:")
                input("Press enter to continue...")
                end = True

        elif op == "3":
            # THIS DELETES CONNECTIONS

            print("Please type a depart country and city, a connection code, an arrival country and city")
            print("WARNING: THIS WILL DELETE ALL ENTRIES RELATED TO THE CONNECTION. PROCEED WITH CAUTION")
            delConnDepCountry = input("Depart Country (code): ")
            delConnDepCity = input("Depart City (code): ")
            delConnCode = input("Connection code: ")
            delConnArrCountry = input("Arrival Country (code): ")
            delConnArrCity = input("Arrival city (code): ")

            codeList = ["21", delConnDepCountry, delConnDepCity, delConnCode, delConnArrCountry, delConnArrCity]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not delete.")
                input("Press enter to continue...")
            else:
                print("Successfully deleted:")
                input("Press enter to continue...")

        elif op == "4":
            # THIS DELETES ROUTES
            print("Please enter a type of train, a train code, a depart country and city, an arrival country and city.")
            print("WARNING: THIS WILL DELETE ALL ENTRIES RELATED TO THE ROUTE. PROCEED WITH CAUTION")
            newRouteTrainType = input("Train type: ")
            newRouteTrainCode = input("Train code: ")
            newRouteDepartCountry = input("Depart country (code): ")
            newRouteDepartCity = input("Depart City (code): ")
            newRouteArrivalCountry = input("Arrival Country (code): ")
            newRouteArrivalCity = input("Arrival City (code): ")

            codeList = ["22", newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not delete.")
                input("Press enter to continue...")
            else:
                print("Successfully deleted:")
                input("Press enter to continue...")

        elif op == "5":

            print("Please type a train type, a train code, a train name, the seats and the origin country and city")
            print("WARNING: THIS WILL DELETE ALL ENTRIES RELATED TO THE TRAIN. PROCEED WITH CAUTION")
            newTrainType = input("Train type (1,2,3,4): ")
            newTrainCode = input("Train code: ")

            codeList = ["23", newTrainType, newTrainCode]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not delete.")
                input("Press enter to continue...")
            else:
                print("Successfully deleted:")
                input("Press enter to continue...")

        elif op == "6":
            end = True

def updates(s):
    end = False
    while not end:
        os.system("cls")
        print("Welcome to update menu. Please, choose and option")
        print("1) Modify price")
        print("2) Modify time")
        print("3) Modify seats")
        print("4) Modify route")
        print("5) Modify train")
        print("6) Modify migratory status")
        print("7) Exit")

        op = input()

        if op == "1":
            # MODIFY PRICE
            correctInt = False
            os.system("cls")
            print("Please enter a type of train, a train code to assign the route to, a depart country and city, an arrival country and city. ")
            newRouteTrainType = input("Train type: ")
            newRouteTrainCode = input("Train code: ")
            newRouteDepartCountry = input("Depart country (code): ")
            newRouteDepartCity = input("Depart City (code): ")
            newRouteArrivalCountry = input("Arrival Country (code): ")
            newRouteArrivalCity = input("Arrival City (code): ")
            newRoutePrice = ""

            while not correctInt:
                try:
                    newRoutePrice = int(input("Price: "))
                    correctInt = True
                    newRoutePrice = str(newRoutePrice)
                except ValueError:
                    print("Please use integers")

            codeList = ["24", newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not update.")
                input("Press enter to continue...")
            else:
                print("Successfully updated:")
                input("Press enter to continue...")


        elif op == "2":
            intCorrect = False
            print("Type a depart country, a city, the connection code and the new time")
            newConnDepCountry = input("Depart Country (code): ")
            newConnDepCity = input("Depart City (code): ")
            newConnCode = input("Connection code: ")
            newConnDuration = ""

            while not intCorrect:
                try:
                    newConnDuration = int(input("Duration (numbers): "))
                    intCorrect = True
                    newConnDuration = str(newConnDuration)
                except ValueError:
                    print("Error, please type an int")

            codeList = ["25", newConnDepCountry, newConnDepCity, newConnCode, newConnDuration]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not update.")
                input("Press enter to continue...")
            else:
                print("Successfully updated:")
                input("Press enter to continue...")


        elif op == "3":
            # UPDATE SEATS

            correctInt = False
            print("Enter type of train and train code.")
            newTrainType = input("Train type (1,2,3,4): ")
            newTrainCode = input("Train code: ")
            newTrainSeats = ""
            while not correctInt:
                try:
                    newTrainSeats = int(input("Seats: "))
                    correctInt = True
                    newTrainSeats = str(newTrainSeats)
                except ValueError:
                    print("Please use integers")

            codeList = ["26", newTrainType, newTrainCode, newTrainSeats]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not update.")
                input("Press enter to continue...")
            else:
                print("Successfully updated:")
                input("Press enter to continue...")

        elif op == "4":
            # UPDATE ROUTE
            os.system("cls")
            print("Please enter a type of train, a train code to assign the route to, a depart country and city, an arrival country and city for searching")
            oldRouteTrainType = input("Train type: ")
            oldRouteTrainCode = input("Train code: ")
            oldRouteDepartCountry = input("Depart country (code): ")
            oldRouteDepartCity = input("Depart City (code): ")
            oldRouteArrivalCountry = input("Arrival Country (code): ")
            oldRouteArrivalCity = input("Arrival City (code): ")

            print("Please enter your new arrival country and city")
            newRouteArrivalCountry = input("Arrival Country (code): ")
            newRouteArrivalCity = input("Arrival City (code): ")

            codeList = ["27", oldRouteTrainType, oldRouteTrainCode, oldRouteDepartCountry, oldRouteDepartCity, oldRouteArrivalCountry, oldRouteArrivalCity, newRouteArrivalCountry, newRouteArrivalCity]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not update.")
                input("Press enter to continue...")
            else:
                print("Successfully updated:")
                input("Press enter to continue...")

        elif op == "5":
            # UPDATE TRAIN

            intCorrect = False
            opCorrect = False
            print("Please type a train type and a train code")
            trainType = input("Train type (1,2,3,4): ")
            trainCode = input("Train code: ")

            print("Enter new values for train")
            newTrainName = input("New Train name: ")

            newTrainCapacity = ""

            while not intCorrect:
                try:
                    newTrainCapacity = int(input("New train capacity: "))
                    intCorrect = True
                    newTrainCapacity = str(newTrainCapacity)
                except ValueError:
                    print("Error, please type an int")

            print("Would you like to relocate this train? Warning: THIS WILL CLEAR ALL ROUTES ASSOCIATED WITH THIS TRAIN")

            while not opCorrect:
                op1 = input("Y/N: ")
                if op1 == "Y" or op1 == "y":
                    opCorrect = True
                    newTrainCountry = input("New Country (code): ")
                    newTrainCity = input("New City (code): ")

                    codeList = ["28", trainType, trainCode, newTrainName, newTrainCapacity, newTrainCountry, newTrainCity]
                    s.send(pickle.dumps(codeList))
                    success = pickle.loads(s.recv(8192))

                    if not success:
                        print("Could not update.")
                        input("Press enter to continue...")
                    else:
                        print("Successfully updated:")
                        input("Press enter to continue...")

                elif op1 == "N" or op1 == "n":
                    opCorrect = True

        elif op == "6":
            # UPDATE MIGRATORY STATEMENT

            print("To change the status, please type de User Id")
            userId = input("User Id")
            userStatus = ""
            while userStatus != "0" or userStatus != "1":
                userStatus = input("User new status (1 or 0): ")

            codeList = ["29", userId, userStatus]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                print("Could not update.")
                input("Press enter to continue...")
            else:
                print("Successfully updated:")
                input("Press enter to continue...")


        elif op == "7":
            end = True

def lastInserts(s):
    codeList = ["30"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def lastDeletes(s):
    codeList = ["31"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getMostUsedRoute(s):
    codeList = ["32"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getLeastUsedRoute(s):
    codeList = ["33"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getMostVisitedCountry(s):
    codeList = ["34"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getMostVisitedCity(s):
    codeList = ["35"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")


def getHighestUsageUser(s):
    codeList = ["36"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getLeastUsageUser(s):
    codeList = ["37"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getUserPurchases(userId, s):
    codeList = ["38", userId]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getHighestUsageTrain(s):
    codeList = ["39"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def getLowestUsageTrain(s):
    codeList = ["40"]
    s.send(pickle.dumps(codeList))
    results = pickle.loads(s.recv(8192))

    if not results:
        print("Not found routes with given parameters. Press enter to re-try.")
        input("Press enter to continue...")
    else:
        print("Found routes:")
        printIterable(results)
        input("Press enter to continue...")

def main():

    """
    MAIN APPLICATION METHOD. INVOKES METHODS ON ADMIN AND USER MODULES

    """

    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))


    global userID, userName
    end_main = False
    reservations = []
    while not end_main:
        os.system('cls')
        print("Welcome to the UTS System. Please, identify yourself by typing an option")
        print("1) User")
        print("2) Admin")
        print("3) Exit UTS")

        op = input()



        # <USER SECTION>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if op == "1":
            userName = "System"
            userID = ""
            grandEnd = False
            logged = False
            loginError = False
            blocked = False

            while not grandEnd:
                os.system('cls')
                print("Welcome. Please choose an option.")
                print("1) Check countries")
                print("2) Check cities")
                print("3) Check connections")
                print("4) Check trains")
                print("5) Check prices")
                print("6) Check train seats")
                print("7) Check routes")
                print("-----------------------------------------------")
                print("8) Reservations")
                print("9) Billing")
                print("-----------------------------------------------")
                print("10) Return")

                op = input("Enter an option: ")

                if op == "1":
                    #CHECK COUNTRIES
                    countryQuerySection(s)
                elif op == "2":
                    #CHECK CITIES
                    cityQuerySection(s)
                elif op == "3":
                    #CHECK CONNECTIONS
                    connectionQuerySection(s)
                elif op == "4":
                    #CHECK TRAINS
                    trainQuerySection(s)
                elif op == "5":
                    #CHECK TRAIN PRICES
                    pricesQuerySection(s)
                elif op == "6":
                    #CHECK TRAIN SEATS
                    seatsQuerySection(s)
                elif op == "7":
                    #CHECK ROUTES
                    routesQuerySection(s)
                elif op == "8":
                    #RESERVATION SECTION
                    while not logged:
                        os.system('cls')
                        if blocked:
                            print("USER IS BLOCKED FROM SYSTEM. STATUS OF 1")
                        if loginError:
                            print("User was not found!! Try Again")
                        print("Welcome. Please type your ID. Type 0 to return.")
                        userId = input("ID: ")

                        if userId != "0":
                            codeList = ["00","", userId]
                            s.send(pickle.dumps(codeList))
                            userValidated = pickle.loads(s.recv(8192))

                            if userValidated:
                                userID = userId
                                codeList = ["01","", userId]
                                s.send(pickle.dumps(codeList))
                                userStatus = pickle.loads(s.recv(8192))
                                if userStatus == "0":

                                    # Set userName here:
                                    codeList = ["02", "", userId]
                                    s.send(pickle.dumps(codeList))
                                    userName = pickle.loads(s.recv(8192))

                                    # Set logged flag
                                    logged = True
                                    loginError = False
                                else:
                                    loginError = False
                                    blocked = True
                            else:
                                loginError = True
                        else:
                            break
                    if logged:
                        reservations = reservationQuerySection(s)
                elif op == "9":
                    #BILLING
                    if logged:
                        billing(s, reservations, userName)
                    else:
                        print("You must be logged to bill.")
                        input("Press enter to continue...")
                elif op == "10":
                    grandEnd = True
                    reservations = []
                    logged = False


        # <ADMIN SECTION>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        elif op == "2":
            adminName = "System"
            adminEnd = False
            logged = False
            loginError = False
            while not logged:
                os.system("cls")
                if loginError:
                    print("Admin was not found!! Try Again")
                print("Welcome. Please type your admin code:")
                code = input("Admin code: ")

                codeList = ["12", code]
                s.send(pickle.dumps(codeList))
                adminValidate = pickle.loads(s.recv(8192))

                if adminValidate:
                    codeList = ["13", code]
                    s.send(pickle.dumps(codeList))
                    adminName = pickle.loads(s.recv(8192))
                    logged = True
                    loginError = False
                else:
                    loginError = True

            while not adminEnd:
                os.system("cls")
                print("Welcome admin: " + adminName + ", please choose an option")
                print("1) Insert")
                print("2) Delete")
                print("3) Update")
                print("4) Check prices")
                print("5) Check connections")
                print("6) Check cities")
                print("7) Check routes")
                print("8) Check Trains")
                print("9) Register Train")
                print("------------------------------")
                print("10) Check countries")
                print("11) Check cities")
                print("12) Check connections")
                print("13) Check trains")
                print("14) Check prices")
                print("15) Check routes")
                print("16) Last inserted")
                print("17) Last train and route deleted")
                print("18) Most used route")
                print("19) Never used route")
                print("20) Most visited country")
                print("21) Most visited city")
                print("22) User that bought the most")
                print("23) User that bought the least")
                print("24) Purchases by user")
                print("25) Most used train")
                print("26) Least used train")
                print("27) Return")

                op = input("Option: ")

                if op == "1":
                    #<INSERTS>
                    inserts(s)
                elif op == "2":
                    #<DELETE>
                    deletes(s)
                elif op == "3":
                    #<UPDATE SECTION>
                    updates(s)
                elif op == "4":
                    #CHECK PRICES
                    pricesQuerySection(s)
                elif op == "5":
                    # CHECK CONNECTIONS
                    connectionQuerySection(s)
                elif op == "6":
                    cityQuerySection(s)
                elif op == "7":
                    # CHECK ROUTES
                    routesQuerySection(s)
                elif op == "8":
                    # CHECK TRAINS
                    trainQuerySection(s)
                elif op == "9":
                    #INSERTS
                    inserts(s)
                elif op == "10":
                    #CHECK COUNTRIES
                    countryQuerySection(s)
                elif op == "11":
                    #CHECK CITIES
                    cityQuerySection(s)
                elif op == "12":
                    #CHECK CONNECTIONS
                    connectionQuerySection(s)
                elif op == "13":
                    #CHECK TRAINS
                    trainQuerySection(s)
                elif op == "14":
                    #CHECK PRICES
                    pricesQuerySection(s)
                elif op == "15":
                    #CHECK ROUTES
                    routesQuerySection(s)
                elif op == "16":
                    #LAST INSERT
                    lastInserts(s)
                elif op == "17":
                    lastDeletes(s)
                elif op == "18":
                    getMostUsedRoute(s)
                elif op == "19":
                    getLeastUsedRoute(s)
                elif op == "20":
                    getMostVisitedCountry(s)
                elif op == "21":
                    getMostVisitedCity(s)
                elif op == "22":
                    getHighestUsageUser(s)
                elif op == "23":
                    getLeastUsageUser(s)
                elif op == "24":
                    userID = input("User ID: ")
                    getUserPurchases(userID, s)
                elif op == "25":
                    getHighestUsageTrain(s)
                elif op == "26":
                    getLowestUsageTrain(s)
                elif op == "27":
                    adminEnd = True


    while True:
        msg = str(input())
        s.send(msg.encode("utf-8"))
if __name__ == '__main__':
    main()