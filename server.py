import _thread as thread
import pickle
import socket
import copy
import itertools

import loadData as data


class SocketServer(socket.socket):
    clients = []

    # This list will be shared by Billing and Reservation Methods. Thus is outside as a global var
    reservations = []
    serverLock = False



    def __init__(self, dat):
        socket.socket.__init__(self)
        #To silence- address occupied!!
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind(('0.0.0.0', 5000))
        self.listen(5)
        self.dat = dat
        self.currentAdminID = ""


    def run(self):
        print("Server started")
        try:
            self.accept_clients()
        except Exception as ex:
            print(ex)
        finally:
            print("Server closed")
            for client in self.clients:
                client.close()
            self.close()

    def accept_clients(self):
        while True:
            (clientsocket, address) = self.accept()
            #Adding client to clients list
            self.clients.append(clientsocket)
            #Client Connected
            self.onopen(clientsocket)
            #Receiving data from client
            thread.start_new_thread(self.receive, (clientsocket,))

    def receive(self, client):
        while 1:

            try:
                dataList = pickle.loads(client.recv(8192))
                self.MANAGEMENTMETHOD(dataList, client)

                if data == '':
                    break
            except Exception:
                print("Error with data receive")
                break

    def MANAGEMENTMETHOD(self, dataList, client):
        """This method will map each request code to the designated method for the server to execute"""
        if dataList[1]==self.currentAdminID:

            if dataList[0] == "00":
                # ValidateUser
                # [0] is code 00
                # [2] is userId
                print(dataList[2])
                returnValue = self.validateUser(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "01":
                # GetUserStatus
                # [0] is code 01
                # [2] is userId
                returnValue = self.getUserStatus(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "02":
                # GetUserName
                # [0] is code 01
                # [2] is userId
                returnValue = self.getUserName(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "03":
                # GetAllCountries
                # [0] is code 03
                returnValue = self.getAllCountries()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "04":
                # GetAllCountries
                # [0] is code 04
                # [2] is op
                returnValue = self.getCitiesByCountry(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "05":
                # getConnectionsByCityAndCountry
                # [0] is code 05
                # [2] is country
                # [3] is city
                returnValue = self.getConnectionsByCityAndCountry(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "06":
                # getTrainByTrainType
                # [0] is code 06
                # [2] is train type code
                returnValue = self.getTrainByTrainType(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "07":
                # getPricesByTrainCode
                # [0] is code 07
                # [2] is train code
                returnValue = self.getPricesByTrainCode(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "08":
                # getPricesByTrainCode
                # [0] is code 08
                # [2] is train code
                returnValue = self.getSeatsByTrainCode(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "09":
                # getRoutesByCity
                # [0] is code 09
                # [2] is city code
                returnValue = self.getRoutesByCity(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "10":
                # getPricesByTrainCode
                # [0] is code 10
                # [2] is country code
                # [3] is city code
                returnValue = self.getRouteForReservations(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "11":
                # recordData
                # [0] is code 11
                # [2] is reservationList
                # [3] is userName
                returnValue = self.recordData(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "12":
                # validateAdmin
                # [0] is code 12
                # [2] is adminCode
                returnValue = self.validateAdmin(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "13":
                # validateAdmin
                # [0] is code 13
                # [2] is adminCode
                returnValue = self.getAdminName(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "14":
                # validateAdmin
                # [0] is code 14
                # [2] is countryCode
                # [3] is countryName
                returnValue = self.insertCountry(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "15":
                # validateAdmin
                # [0] is code 15
                # [2] is countryCode
                # [3] is cityCode
                # [4] is cityName
                returnValue = self.insertCity(dataList[2], dataList[3], dataList[4])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "16":
                # validateAdmin
                # [0] is code 16
                # [2] is depCountryCode
                # [3] is depCityCode
                # [4] is connCode
                # [5] is arrCountryCode
                # [6] is arrCityCode
                # [7] is connDuration
                returnValue = self.insertConnections(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "17":
                # validateAdmin
                # [0] is code 17
                # [2] is the trainType
                # [3] is the trainCode
                # [4] is depCountryCode
                # [5] is depCityCode
                # [6] is arrCountryCode
                # [7] is arrCityCode
                # [8] is the duration
                returnValue = self.insertRoute(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "18":
                # validateAdmin
                # [0] is code 18
                # [2] is the newTrainType
                # [3] is the newTrainCode
                # [4] is newTrainName
                # [5] is newTrainSeats
                # [6] is newTrainCountry
                # [7] is newTrainCity
                returnValue = self.insertTrain(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "19":
                # validateAdmin
                # [0] is code 19
                # [2] is countryToDel
                returnValue = self.deleteCountry(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "20":
                # validateAdmin
                # [0] is code 20
                # [2] is countryToDel
                returnValue = self.deleteCity(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "21":
                # validateAdmin
                # [0] is code 21
                # [2] is delConnDepCountry
                # [3] delConnDepCity
                # [4] delConnCode
                # [5] delConnArrCountry
                # [6] delConnArrCity
                returnValue = self.deleteConnection(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "22":
                # validateAdmin
                # [0] is code 22
                # [2] newRouteTrainType
                # [3] newRouteTrainCode
                # [4] newRouteDepartCountry
                # [5] newRouteDepartCity
                # [6] newRouteArrivalCountry
                # [7] newRouteArrivalCity
                returnValue = self.deleteRoute(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "23":
                # validateAdmin
                # [0] is code 23
                # [2] is newTrainType
                # [3] newTrainCode
                returnValue = self.deleteTrain(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "24":
                # validateAdmin
                # [0] is code 24
                # [2] newRouteTrainType
                # [3] newRouteTrainCode
                # [4] newRouteDepartCountry
                # [5] newRouteDepartCity
                # [6] newRouteArrivalCountry
                # [7] newRouteArrivalCity
                # [8] newRoutePrice
                returnValue = self.updatePrice(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "25":
                # validateAdmin
                # [0] is code 25
                # [2] newConnDepCountry
                # [3] newConnDepCity
                # [4] newConnCode
                # [5] newConnDuration
                returnValue = self.updateTime(dataList[2], dataList[3], dataList[4], dataList[5])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "26":
                # validateAdmin
                # [0] is code 26
                # [2] newTrainType
                # [3] newTrainCode
                # [4] newTrainSeats
                returnValue = self.updateSeats(dataList[2], dataList[3], dataList[4])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "27":
                # validateAdmin
                # [0] is code 27
                # [2] oldRouteTrainType
                # [3] oldRouteTrainCode
                # [4] oldRouteDepartCountry
                # [5] oldRouteDepartCity
                # [6] oldRouteArrivalCountry
                # [7] oldRouteArrivalCity
                # [8] newRouteArrivalCountry
                # [9] newRouteArrivalCity
                returnValue = self.updateRoute(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8], dataList[9])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "28":
                # validateAdmin
                # [0] is code 28
                # [2] trainType
                # [3] trainCode
                # [4] newTrainName
                # [5] newTrainCapacity
                # [6] newTrainCountry
                # [7] newTrainCity
                returnValue = self.updateTrain(dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "29":
                # validateAdmin
                # [0] is code 29
                # [2] trainType
                # [3] trainCode
                returnValue = self.updateMigratoryStatus(dataList[2], dataList[3])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "30":
                # validateAdmin
                # [0] is code 30
                returnValue = self.lastInserts()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "31":
                # validateAdmin
                # [0] is code 31
                returnValue = self.lastDeletes()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "32":
                # validateAdmin
                # [0] is code 32
                returnValue = self.dat.getMostUsedRoute()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "33":
                # validateAdmin
                # [0] is code 33
                returnValue = self.dat.getLeastUsedRoute()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "34":
                # validateAdmin
                # [0] is code 34
                returnValue = self.dat.getMostVisitedCountry()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "35":
                # validateAdmin
                # [0] is code 35
                returnValue = self.dat.getMostVisitedCity()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "36":
                # validateAdmin
                # [0] is code 36
                returnValue = self.dat.getHighestUsageUser()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "37":
                # validateAdmin
                # [0] is code 37
                returnValue = self.dat.getLeastUsageUser()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "38":
                # validateAdmin
                # [0] is code 38
                # [2] is userID
                returnValue = self.dat.getUserPurchases(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "39":
                # validateAdmin
                # [0] is code 39
                returnValue = self.dat.getHighestUsageTrain()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "40":
                # validateAdmin
                # [0] is code 40
                returnValue = self.dat.getLowestUsageTrain()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "41":
                # validateAdmin
                # [0] is code 41
                returnValue = self.getCustomRoutes(dataList[2], dataList[3], dataList[4], dataList[5])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "42":
                # getCountryByCode
                # [2] is countryCode
                returnValue = self.getCountryByCode(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "43":
                # getAllTrains
                returnValue = self.getAllTrains()
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "44":
                # getAllCities
                returnValue = self.getAllCities()
                client.send(pickle.dumps(returnValue))
            elif dataList[0] == "45":
                # LOCK_SERVER_ADMIN
                self.lockServerForAdmin(dataList[2])
            elif dataList[0] == "46":
                # UNLOCK_SERVER_ADMIN
                self.unlockServerForAdmin()

            elif dataList[0] == "47":
                # getCountryByCode
                # [2] is countryCode
                returnValue = self.getAttractionsByCountry(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "48":
                # getCountryByCode
                # [2] is cityCode
                returnValue = self.getAttractionsByCity(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "49":
                # getCountryByCode
                # [2] is attractionCode
                returnValue = self.getAttractionsByAttractionCode(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "50":
                # getCountryByCode
                # [2] is trainType
                returnValue = self.insertTrainType(dataList[2])
                client.send(pickle.dumps(returnValue))

            elif dataList[0] == "51":
                # getCountryByCode
                # [2] is trainType
                returnValue = self.getTrainTypes(dataList[2])
                client.send(pickle.dumps(returnValue))

        else:
            returnValue = "1"
            client.send(pickle.dumps(returnValue))




    # User validation Method. Checks if user exists
    def validateUser(self, userId):
        """Method returns true if user found. Else false
        :param userId is the user id to look for."""
        for i in range(len(self.dat.users)):
            if userId in self.dat.users[i]:
                print(self.dat.users[i])
                return True

    def getUserStatus(self, userId):
        """Method returns an user status of 1 or 0
        :param userId is the user id to search for"""
        for i in range(len(self.dat.users)):
            if userId in self.dat.users[i]:
                userStatus = self.dat.users[i][4]
                return userStatus

    def getUserName(self, userId):
        """:returns userName for given user
         :param userId is the user id to search for"""
        for i in range(len(self.dat.users)):
            if userId in self.dat.users[i]:
                userName = self.dat.users[i][3]
                return userName

    def getAllCountries(self):
        """Return a list with all the found countries on the data object instance"""
        returnList = []
        for i in range(len(self.dat.countryCitiesConnections)):
            returnList.append([self.dat.countryCitiesConnections[i][0], self.dat.countryCitiesConnections[i][1]])
        return returnList

    def getCitiesByCountry(self, countryCode):
        """Returns cities by country
        :param countryCode is the op provided by user"""
        returnList = []
        for i in self.dat.countryCitiesConnections:
            if i[0]==countryCode:
                if i[2]:
                    for j in i[2]:
                        returnList.append([j[0], j[1]])
        return returnList

    def getConnectionsByCityAndCountry(self, country, city):
        """Returns connections by country and city
        :param country is the country code
        :param city is the city code"""
        count = 1
        returnList = []
        for i in range(len(self.dat.countryCitiesConnections)):
            for j in range(len(self.dat.countryCitiesConnections[i][2])):
                for k in range(len(self.dat.countryCitiesConnections[i][2][j][2])):
                    if self.dat.countryCitiesConnections[i][0] == country:
                        if self.dat.countryCitiesConnections[i][2][j][0] == city:
                            returnList.append( str(
                                self.dat.countryCitiesConnections[i][2][j][2][k][0]) + ". From: " + str(
                                self.dat.countryCitiesConnections[i][0]) + ", " + str(
                                self.dat.countryCitiesConnections[i][2][j][0]) + "; to " + str(
                                self.dat.countryCitiesConnections[i][2][j][2][k][1]) + ", " + str(
                                self.dat.countryCitiesConnections[i][2][j][2][k][2]) + ". Duration: " + str(
                                self.dat.countryCitiesConnections[i][2][j][2][k][3]))
                            count += 1
        return returnList

    def getTrainByTrainType(self, train):
        """Returns all trais by given train type
        :param train is the train type code"""
        returnList = []
        if train != "0":
            if len(train) < 2:
                train = "0" + train
            for i in range(len(self.dat.trainRoutes)):
                if train == self.dat.trainRoutes[i][0]:
                    returnList.append(" Code: " + self.dat.trainRoutes[i][1] + ". Name: " + self.dat.trainRoutes[i][2] + ". Capacity: " + self.dat.trainRoutes[i][3])
        return returnList

    def getPricesByTrainCode(self, train):
        """Returns a the price of the specified train route
         :param train is the train code"""
        returnList = []
        if train != "0":
            for i in range(len(self.dat.trainRoutes)):
                for j in range(len(self.dat.trainRoutes[i][6])):
                    if train == self.dat.trainRoutes[i][1]:
                        returnList.append(
                            "Cost: " + self.dat.trainRoutes[i][6][j][4] + ". Train Code: " + self.dat.trainRoutes[i][
                                1] + ". Name: " +
                            self.dat.trainRoutes[i][2] + ". Goes from " + self.dat.trainRoutes[i][6][j][0] + ", " +
                            self.dat.trainRoutes[i][6][j][1] + " to " + self.dat.trainRoutes[i][6][j][2] + ", " +
                            self.dat.trainRoutes[i][6][j][3])
        return returnList

    def getSeatsByTrainCode(self, train):
        """This method returns a list of seats by train
        :param train is the train code"""
        returnList = []
        if train != "0":
            for i in range(len(self.dat.trainRoutes)):
                if train == self.dat.trainRoutes[i][1]:
                    returnList.append("Train: " + self.dat.trainRoutes[i][1] + ". Seats: " + self.dat.trainRoutes[i][3])
        return returnList

    def getRoutesByCity(self, city):
        """Returns the connections of a city.
        :param city is the city code"""
        returnList = []
        count = 0
        if city != "0":
            for i in range(len(self.dat.trainRoutes)):
                for j in range(len(self.dat.trainRoutes[i][6])):
                    if city == self.dat.trainRoutes[i][6][j][1]:
                        count += 1
                        returnList.append("Train Code: " + self.dat.trainRoutes[i][
                            1] + ". Goes from " + self.dat.trainRoutes[i][6][j][0] + ", " +
                              self.dat.trainRoutes[i][6][j][1] + " to " + self.dat.trainRoutes[i][6][j][2] + ", " +
                              self.dat.trainRoutes[i][6][j][3])
        return returnList

    def getRouteForReservations(self, selectedCountry, selectedCity):
        """Returns a list of routes for reservations
        :param selectedCountry is the selected country code
        :param selectedCity is the selected city code"""
        returnList = []
        for i in range(len(self.dat.trainRoutes)):
            for j in range(len(self.dat.trainRoutes[i][6])):
                if self.dat.trainRoutes[i][6][j][0] == selectedCountry and self.dat.trainRoutes[i][6][j][1] == selectedCity:
                    returnList.append([self.dat.trainRoutes[i][0], self.dat.trainRoutes[i][1], self.dat.trainRoutes[i][2], self.dat.trainRoutes[i][6][j][0], self.dat.trainRoutes[i][6][j][1], self.dat.trainRoutes[i][6][j][2], self.dat.trainRoutes[i][6][j][3], self.dat.trainRoutes[i][6][j][4], self.dat.trainRoutes[i][3]])
        return returnList

    def recordData(self, reservations, userName):
        """Returns a confirmation for appendage of reservation data
        :param reservations is the reservations to insert list
        :param userName is the userName"""
        numOfTrips = len(reservations)
        dt.addUserTravelCount(userName, numOfTrips)
        success = False
        for i in reservations:
            self.dat.addCityCount(i[5], i[6])
            self.dat.addCountryCount(i[5])
            self.dat.addRoutesCount(i[0], i[1], i[3], i[4], i[5], i[6])
            self.dat.addTrainCount(i[0], i[1])
            self.dat.reduceSeatsBy(i[9], i[0], i[1])
            success = True
        return success

    def validateAdmin(self, adminCode):
        """Check for admin to exists. Returns true if found
        :param adminCode is the admin code"""
        found = False
        for i in self.dat.admin:
            if i[0] == adminCode:
                found = True
                break
        return found

    def getAdminName(self, adminCode):
        """Returns the admin name
        :param adminCode is the admin code"""
        adminName = ""
        for i in self.dat.admin:
            if i[0] == adminCode:
                adminName = i[1]
                break
        return adminName

    def insertCountry(self, newCountryCode, newCountryName):
        """Inserts a new country
        :param newCountryName is the new country name
        :param newCountryCode is the new country code"""
        presentCountry = False
        success = False
        for i in self.dat.countryCitiesConnections:
            if i[0] == newCountryCode or i[1] == newCountryName:
                presentCountry = True
                break

        if not presentCountry:
            self.dat.countryCitiesConnections += [[newCountryCode, newCountryName, []]]
            self.dat.countriesByUsage.append([[newCountryCode, newCountryName], 0])
            self.dat.lastCountryInsert = [newCountryCode, newCountryName]
            success = True
        print(self.dat.countryCitiesConnections)
        return success

    def insertCity(self, countryCodeForCity, newCityCode, newCityName):
        """Inserts a new city
        :param countryCodeForCity is the country where the city belongs
        :param newCityCode is the new city code
        :param newCityName is the new city name"""
        presentCity = False
        success = False
        for i in self.dat.countryCitiesConnections:
            for j in i[2]:
                if i[0] == countryCodeForCity and (j[0] == newCityCode or j[1] == newCityName):
                    presentCity = True
                    break

        if not presentCity:
            for i in self.dat.countryCitiesConnections:
                if i[0] == countryCodeForCity:
                    i[2] += [[newCityCode, newCityName, []]]
                    self.dat.citiesByUsage.append([[countryCodeForCity, [newCityCode, newCityName]], 0])
                    self.dat.lastCityInsert = [countryCodeForCity, newCityCode, newCityName]
                    success = True
        return success

    def insertConnections(self, newConnDepCountry, newConnDepCity, newConnCode, newConnArrCountry, newConnArrCity, newConnDuration):
        """Inserts a new connection
        :param newConnDepCountry is the departure country for the connection
        :param newConnDepCity is the the departure city for the connection
        :param newConnCode is the connection identifier
        :param newConnArrCountry is the arrival country of the connection
        :param newConnArrCity is the arrival city of the connection
        :param newConnDuration is the length in time of the connection"""
        presentConnection = False
        success = False
        for i in self.dat.countryCitiesConnections:
            for j in i[2]:

                if i[0] == newConnDepCountry and j[0] == newConnDepCity:
                    # Depart city or country do exist

                    if data.countryAndCityExistInList(newConnArrCountry, newConnArrCity, self.dat.countryCitiesConnections):
                        # Arrive city or country do exist

                        possibleConnections = self.dat.getConnectionById(self.dat.countryCitiesConnections, newConnCode)
                        if len(possibleConnections) > 0:
                            presentConnection = True
                            break

        if not presentConnection:
            for i in self.dat.countryCitiesConnections:
                for j in i[2]:
                    if i[0] == newConnDepCountry and j[0] == newConnDepCity:
                        j[2] += [[newConnCode, newConnArrCountry, newConnArrCity, newConnDuration]]
                        self.dat.lastConnectionInsert = [newConnCode, newConnArrCountry, newConnArrCity, newConnDuration]
                        success = True
        return success

    def insertRoute(self, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice):
        """Inserts a new route to the system
        :param newRouteTrainType is the train type
        :param newRouteTrainCode is the train code or id
        :param newRouteDepartCountry is the depart country
        :param newRouteDepartCity is the depart city code
        :param newRouteArrivalCountry is the new arrival cuntry code
        :param newRouteArrivalCity is the new arrival city code
        :param newRoutePrice is the new route price"""
        presentRoute = False
        accepted = False
        success = False
        if data.countryAndCityExistInList(newRouteArrivalCountry, newRouteArrivalCity, self.dat.countryCitiesConnections):
            accepted = True
        for i in self.dat.trainRoutes:
            if i[6]:
                for j in i[6]:
                    if i[0] == newRouteTrainType and i[1] == newRouteTrainCode and i[4] == newRouteDepartCountry and i[5] == newRouteDepartCity and j[0] == newRouteDepartCountry and j[1] == newRouteDepartCity and j[2] == newRouteArrivalCountry and j[3] == newRouteArrivalCity:
                        presentRoute = True
                        break

        if not presentRoute:
            if accepted:
                for i in self.dat.trainRoutes:
                    if i[0] == newRouteTrainType and i[1] == newRouteTrainCode and i[4] == newRouteDepartCountry and i[5] == newRouteDepartCity:
                        i[6] += [[newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]]
                        self.dat.routesByUsage.append([[newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity], 0])
                        self.dat.lastRouteInsert = [newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity]
                        success = True

        return success

    def insertTrain(self, newTrainType, newTrainCode, newTrainName, newTrainSeats, newTrainCountry, newTrainCity):
        """Inserts a train to the system
        :param newTrainType is the new train type
        :param newTrainCode is the new train code to insert
        :param newTrainName is the train name
        :param newTrainSeats is the amount of seats the train will have
        :param newTrainCountry is the new train country location
        :param newTrainCity is the new train city location"""
        trainPresent = False
        accepted = False
        success = False
        if data.countryAndCityExistInList(newTrainCountry, newTrainCity, self.dat.countryCitiesConnections):
            accepted = True
        for i in self.dat.trainRoutes:
            if i[0] == newTrainType and i[1] == newTrainCode:
                trainPresent = True

        if not trainPresent:
            if accepted:
                self.dat.trainRoutes += [[newTrainType, newTrainCode, newTrainName, newTrainSeats, newTrainCountry, newTrainCity, []]]
                self.dat.trainsByUsage.append([[newTrainType, newTrainCode, newTrainName], 0])
                self.dat.lastTrainInsert = [newTrainType, newTrainCode, newTrainName]
                success = True

        return success



    def deleteCountry(self, countryToDel):
        """This query deletes a given country an all of its information. HANDLE WITH CARE
        :param countryToDel is the country code to delete"""
        success = False
        if data.countryExistsInList(countryToDel, self.dat.countryCitiesConnections):
            trainRoutesHolder = []
            countryCityConnectionsHolder = []

            for i in self.dat.trainRoutes:
                if i[6]:
                    for j in i[6]:
                        if not (j[0] == countryToDel or j[2] == countryToDel):
                            trainRoutesHolder.append(i)
                else:
                    if not i[4] == countryToDel:
                        trainRoutesHolder.append(i)

            for i in self.dat.countryCitiesConnections:
                if not i[0] == countryToDel:
                    countryCityConnectionsHolder.append(i)

            countryCityConnectionsHolder2 = copy.deepcopy(countryCityConnectionsHolder)
            for i in countryCityConnectionsHolder:
                for j in i[2]:
                    j[2] = []

            for i in range(len(countryCityConnectionsHolder2)):
                for j in range(len(countryCityConnectionsHolder2[i][2])):
                    for k in countryCityConnectionsHolder2[i][2][j][2]:
                        if not countryToDel in k:
                            countryCityConnectionsHolder[i][2][j][2] += [k]

            self.dat.countryCitiesConnections = countryCityConnectionsHolder
            self.dat.trainRoutes = trainRoutesHolder

            # Deletes in reports
            reportsCountryInsert = self.dat.deleteCountryReports(countryToDel)
            self.dat.countriesByUsage = reportsCountryInsert
            success = True

        return success

    def deleteCity(self, countryCode, cityToDelete):
        """Deletes a provided city. HANDLE WITH CARE
        :param countryCode country to look for
        :param cityToDelete is the city code to kaboom"""
        success = False
        if data.countryAndCityExistInList(countryCode, cityToDelete, self.dat.countryCitiesConnections):
            trainRoutesHolder = []

            for i in self.dat.trainRoutes:
                if not cityToDelete in i:
                    trainRoutesHolder.append(i)

            countryCityConnectionsHolder2 = copy.deepcopy(self.dat.countryCitiesConnections)
            for i in self.dat.countryCitiesConnections:
                i[2] = []

            for i in range(len(countryCityConnectionsHolder2)):
                for k in countryCityConnectionsHolder2[i][2]:
                    if not cityToDelete in k:
                        self.dat.countryCitiesConnections[i][2].append(k)

            countryCityConnectionsHolder2 = copy.deepcopy(self.dat.countryCitiesConnections)
            for i in range(len(self.dat.countryCitiesConnections)):
                for j in range(len(self.dat.countryCitiesConnections[i][2])):
                    self.dat.countryCitiesConnections[i][2][j][2] = []

            for i in range(len(countryCityConnectionsHolder2)):
                if self.dat.countryCitiesConnections[i][2]:
                    for j in range(len(countryCityConnectionsHolder2[i][2])):
                        for k in range(len(countryCityConnectionsHolder2[i][2][j][2])):
                            if not cityToDelete in countryCityConnectionsHolder2[i][2][j][2][k]:
                                self.dat.countryCitiesConnections[i][2][j][2].append(countryCityConnectionsHolder2[i][2][j][2][k])

            self.dat.trainRoutes = trainRoutesHolder

            # Delete on reports
            cityReportsDel = self.dat.deleteCityReports(countryCode, cityToDelete)
            self.dat.citiesByUsage = cityReportsDel
            success = True

        return success

    def deleteConnection(self, delConnDepCountry, delConnDepCity, delConnCode, delConnArrCountry, delConnArrCity):
        """This method deletes a given connection
        :param delConnDepCountry is the depart country
        :param delConnDepCity is the dep city
        :param delConnCode is the connCode
        :param delConnArrCountry is the arrival delete country
        :param delConnArrCity is the arrive city"""
        success = True
        if self.dat.connectionFullExists(delConnDepCountry, delConnDepCity, delConnArrCountry, delConnArrCity) and self.dat.getConnectionId(delConnDepCountry, delConnDepCity, delConnArrCountry, delConnArrCity) == delConnCode:
            trainRoutesHolder = copy.deepcopy(self.dat.trainRoutes)
            countryCityConnectionsHolder = copy.deepcopy(self.dat.countryCitiesConnections)

            # Empty Routes
            for i in self.dat.trainRoutes:
                i[6] = []

            for i in range(len(trainRoutesHolder)):
                for j in range(len(trainRoutesHolder[i][6])):
                    if not (trainRoutesHolder[i][6][j][0] == delConnDepCountry and trainRoutesHolder[i][6][j][1] == delConnDepCity and trainRoutesHolder[i][6][j][2] == delConnArrCountry and trainRoutesHolder[i][6][j][3] == delConnArrCity):
                        self.dat.trainRoutes[i][6].append(trainRoutesHolder[i][6][j])

            for i in range(len(self.dat.countryCitiesConnections)):
                for j in range(len(self.dat.countryCitiesConnections[i][2])):
                    self.dat.countryCitiesConnections[i][2][j][2] = []

            print(countryCityConnectionsHolder)
            for i in range(len(countryCityConnectionsHolder)):
                if self.dat.countryCitiesConnections[i][2]:
                    for j in range(len(countryCityConnectionsHolder[i][2])):
                        for k in range(len(countryCityConnectionsHolder[i][2][j][2])):
                            print(countryCityConnectionsHolder[i][2][j][2])
                            if not (countryCityConnectionsHolder[i][2][j][2][k][0] == delConnCode and delConnArrCountry == countryCityConnectionsHolder[i][2][j][2][k][1] and delConnArrCity == countryCityConnectionsHolder[i][2][j][2][k][2]):
                                self.dat.countryCitiesConnections[i][2][j][2].append(countryCityConnectionsHolder[i][2][j][2][k])

            success = True

        return success

    def deleteRoute(self, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity):
        """This deletes routes. Handle with care"""
        trainRoutesHolder = copy.deepcopy(self.dat.trainRoutes)
        success = True
        # Empty Routes
        if data.countryAndCityExistInList(newRouteDepartCountry, newRouteDepartCity, self.dat.countryCitiesConnections):
            for i in self.dat.trainRoutes:
                i[6] = []

            for i in range(len(trainRoutesHolder)):
                for j in range(len(trainRoutesHolder[i][6])):
                    if not (trainRoutesHolder[i][0] == newRouteTrainType and trainRoutesHolder[i][1] == newRouteTrainCode and trainRoutesHolder[i][6][j][0] == newRouteDepartCountry and trainRoutesHolder[i][6][j][1] == newRouteDepartCity and trainRoutesHolder[i][6][j][
                        2] == newRouteArrivalCountry and
                            trainRoutesHolder[i][6][j][3] == newRouteArrivalCity):
                        self.dat.trainRoutes[i][6].append(trainRoutesHolder[i][6][j])

        if trainRoutesHolder == self.dat.trainRoutes:
            pass
        else:
            self.dat.lastDeletedRoute = [newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity]
            success = True
        return success

    def deleteTrain(self, newTrainType, newTrainCode):
        """This method deletes trains. Handle with care"""
        trainRoutesHolder = []
        success = False
        for i in self.dat.trainRoutes:
            if not (i[0] == newTrainType and i[1] == newTrainCode):
                trainRoutesHolder.append(i)

        self.dat.trainRoutes = trainRoutesHolder
        if self.dat.trainRoutes == trainRoutesHolder:
            pass
        else:
            self.dat.lastDeletedTrain = [newTrainType, newTrainCode]
            listForReportsTrain = self.dat.deleteTrainForReports(newTrainType, newTrainCode)
            self.dat.trainsByUsage = listForReportsTrain
            success = True
        return success

    def updatePrice(self, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice):
        """Updates the prices of a route"""
        found = False
        for i in self.dat.trainRoutes:
            for k in i[6]:
                if i[0] == newRouteTrainType and i[1] == newRouteTrainCode and k[0] == newRouteDepartCountry and k[1] == newRouteDepartCity and k[2] == newRouteArrivalCountry and k[3] == newRouteArrivalCity:
                    k[4] = newRoutePrice
                    found = True

        return found

    def updateTime(self, newConnDepCountry, newConnDepCity, newConnCode, newConnDuration):
        found = False
        for i in self.dat.countryCitiesConnections:
            if i[0] == newConnDepCountry:
                for j in i[2]:
                    if j[0] == newConnDepCity:
                        for k in j[2]:
                            if k[0] == newConnCode:
                                found = True
                                k[3] = newConnDuration

        return found

    def updateSeats(self, newTrainType, newTrainCode, newTrainSeats):
        found = False
        for i in self.dat.trainRoutes:
            if i[0] == newTrainType and i[1] == newTrainCode:
                found = True
                i[3] = newTrainSeats

        return found

    def updateRoute(self, oldRouteTrainType, oldRouteTrainCode, oldRouteDepartCountry, oldRouteDepartCity, oldRouteArrivalCountry, oldRouteArrivalCity, newRouteArrivalCountry, newRouteArrivalCity):
        success = False
        if self.dat.connectionFullExists(oldRouteDepartCountry, oldRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity):
            for i in self.dat.trainRoutes:
                if i[0] == oldRouteTrainType and i[1] == oldRouteTrainCode:
                    for j in i[6]:
                        if j[0] == oldRouteDepartCountry and j[1] == oldRouteDepartCity and j[2] == oldRouteArrivalCountry and j[3] == oldRouteArrivalCity:
                            j[0] = oldRouteDepartCountry
                            j[1] = oldRouteDepartCity
                            j[2] = newRouteArrivalCountry
                            j[3] = newRouteArrivalCity
                            success = True

            for i in self.dat.routesByUsage:
                if i[0][0] == oldRouteTrainType and i[0][1] == oldRouteTrainCode and i[0][3] == oldRouteDepartCountry and i[0][4] == oldRouteDepartCity and i[0][5] == oldRouteArrivalCountry and i[0][6] == oldRouteArrivalCity:
                    i[0][3] = oldRouteDepartCountry
                    i[0][4] = oldRouteDepartCity
                    i[0][5] = newRouteArrivalCountry
                    i[0][6] = newRouteArrivalCity


        return success

    def updateTrain(self, trainType, trainCode, newTrainName, newTrainCapacity, newTrainCountry, newTrainCity):
        """Updates the values of the trains"""
        success = False
        if data.countryAndCityExistInList(newTrainCountry, newTrainCity, self.dat.countryCitiesConnections):
            for i in self.dat.trainRoutes:
                if i[0] == trainType and i[1] == trainCode:
                    i[2] = newTrainName
                    i[3] = newTrainCapacity
                    i[4] = newTrainCountry
                    i[5] = newTrainCity
                    # CLEAR ROUTES
                    i[6] = []

            routesByUsageHolder = []
            # Delete from routes reports list
            for i in range(len(self.dat.routesByUsage)):
                if not (self.dat.routesByUsage[i][0][0] == trainType and self.dat.routesByUsage[i][0][1] == trainCode):
                    routesByUsageHolder.append(self.dat.routesByUsage[i])

            self.dat.routesByUsage = routesByUsageHolder

            # Modify from trains reports list
            for i in self.dat.trainsByUsage:
                if i[0][0] == trainType and i[0][1] == trainCode:
                    print("here")
                    i[0][2] = newTrainName

            success = True

        return success

    def updateMigratoryStatus(self, userId, userStatus):
        """Updates the migratory status of an user"""
        success = False
        for i in self.dat.users:
            if i[2] == userId:
                i[4] = userStatus
                success = True
        return success


    def lastInserts(self):
        """Returns latest inserts"""
        returnList = []
        if self.dat.lastCountryInsert:
            returnList.append("Last inserted country: " + self.dat.lastCountryInsert[0] + ", " + self.dat.lastCountryInsert[1])
        if self.dat.lastCityInsert:
            returnList.append("Last inserted city: " + self.dat.lastCityInsert[0] + ", " + self.dat.lastCityInsert[1] + ", " + self.dat.lastCityInsert[2])
        if self.dat.lastRouteInsert:
            returnList.append("Last inserted route: " + self.dat.lastRouteInsert[0] + ", " + self.dat.lastRouteInsert[1] + ". From " + self.dat.lastRouteInsert[2] + ", " + self.dat.lastRouteInsert[3] + ", To" + self.dat.lastRouteInsert[4] + ", " + self.dat.lastRouteInsert[5])
        if self.dat.lastConnectionInsert:
            returnList.append("Last inserted connection: " + self.dat.lastRouteInsert[0] + ", " + self.dat.lastRouteInsert[1] + ", " + self.dat.lastRouteInsert[2] + ", " + self.dat.lastRouteInsert[3])
        if self.dat.lastTrainInsert:
            returnList.append("Last train city: " + self.dat.lastTrainInsert[0] + ", " + self.dat.lastTrainInsert[1] + ", " + self.dat.lastTrainInsert[2])
        return returnList

    def lastDeletes(self):
        """Returns latest deletes"""
        returnList = []
        if self.dat.lastDeletedRoute:
            returnList.append("Last deleted route: " + self.dat.lastDeletedRoute[0] + ", " + self.dat.lastDeletedRoute[1] + ". From " + self.dat.lastDeletedRoute[2] + ", " + self.dat.lastDeletedRoute[3] + ", To" + self.dat.lastDeletedRoute[4] + ", " + self.dat.lastDeletedRoute[5])
        if self.dat.lastDeletedTrain:
            returnList.append("Last deleted train: " + self.dat.lastDeletedTrain[0] + ", " + self.dat.lastDeletedTrain[1])
        return returnList


    def getCustomRoutes(self, depCountry, depCity, arrCountry, arrCity):
        """Returns custom routes for user selections"""
        OdepCountry = depCountry
        OdepCity = depCity
        OarrCountry = arrCountry
        OarrCity = arrCity


        routeList = []
        for i in self.dat.trainRoutes:
            if i[6]:
                for j in i[6]:
                    routeList.append(j)


        permList = []
        for i in itertools.permutations(routeList): permList.append(list(i))

        realLists = []
        for i in permList:
            tempList = []
            depCountry = OdepCountry
            depCity = OdepCity
            arrCountry = OarrCountry
            arrCity = OarrCity
            for j in i:
                if depCountry==arrCountry and depCity==arrCity:
                    break
                else:
                    if (j[0] == depCountry and j[1] == depCity) and (j[2]!=OdepCountry and j[3]!=OdepCity):
                        tempList.append(j)
                        depCountry = j[2]
                        depCity = j[3]
            depCountry = OdepCountry
            depCity = OdepCity
            arrCountry = OarrCountry
            arrCity = OarrCity
            if len(tempList)==1:
                if tempList[0]==depCountry and tempList[1]==depCity and tempList[2]==arrCountry and tempList[3]==arrCity:
                    if tempList not in realLists:
                        realLists.append(tempList)
            else:
                if tempList not in realLists:
                    realLists.append(tempList)


        for i in realLists:
            distance=0
            for j in i:
                connId = self.dat.getConnectionId(j[0], j[1], j[2], j[3])
                distance += int(self.dat.getConnectionById(self.dat.countryCitiesConnections, connId)[0][5])
            i.append(distance)



        finalList = []
        for i in realLists:
            print(i)
            tempFinalList = []
            for j in self.dat.trainRoutes:
                for k in j[6]:
                    if k == i[0]:
                        tempFinalList.append(j[:6]+[i[0]])
                    elif k==i[1]:
                        tempFinalList.append(j[:6]+[i[1]])
            tempFinalList.append(i[len(i)-1])
            finalList.append(tempFinalList)


        return finalList

    def getCountryByCode(self, countryCode):
        """Returns a country name as standalone string
        :param countryCode is the code of the country to search for"""
        result = ""
        for i in self.dat.countryCitiesConnections:
            print(i[0])
            if i[0]==countryCode:
                result = i[1]
                break
        return result

    def getAllTrains(self):
        """Returns a list with all present trains on system"""
        result = []
        for i in self.dat.trainRoutes:
            result.append(i[:6])
        return result

    def getAllCities(self):
        """Returns a list with all cities in the system"""
        result = []
        for i in self.dat.countryCitiesConnections:
            for j in i[2]:
                result.append(j[:2])
        return result

    def lockServerForAdmin(self, adminId):
        """Sets the current admin admin code to the specified admin"""
        print("here in method")
        print(adminId)
        print(self.currentAdminID)
        self.currentAdminID = adminId
        print(self.currentAdminID)
        print("Locked")

    def unlockServerForAdmin(self):
        """Unlocks server for all to use"""
        print(self.currentAdminID)
        self.currentAdminID = ""
        print(self.currentAdminID)
        print("Unlocked")

    def getAttractionsByCountry(self, countryCode):
        """Returns all attractions for selected country
        :param countryCode is the selection country code"""
        result = []
        for i in self.dat.attractions:
            if i[0] == countryCode:
                result.append(i)
        return result

    def getAttractionsByCity(self, cityCode):
        """Returns all attractions for selected city
        :param cityCode is the selection country code"""
        result = []
        for i in self.dat.attractions:
            if i[1] == cityCode:
                result.append(i)
        return result

    def getAttractionsByAttractionCode(self, attractionCode):
        """Returns all attractions for selected attraction code
        :param attractionCode is the selection country code"""
        result = []
        for i in self.dat.attractions:
            if i[2] == attractionCode:
                result.append(i)
        return result

    def insertTrainType(self, trainType):
        """Insert a train type to the list
        :param trainType is the train type to insert"""
        success = False
        found = False
        for i in self.dat.trainTypes:
            if i == trainType:
                found = True
                break

        if not found:
            success = True
            self.dat.trainTypes.append(trainType)

        return success

    def getTrainType(self):
        """Returns all train types"""
        result = []
        for i in self.dat.trainTypes:
            i.append(result)
        return result


    def broadcast(self, message):
        #Sending message to all clients
        for client in self.clients:
            client.send(message)

    def onopen(self, client):
        pass

    def onmessage(self, client, message):
        pass

    def onclose(self, client):
        pass



class BasicChatServer(SocketServer):

    def __init__(self, dat):
        SocketServer.__init__(self, dat)

    def onmessage(self, client, message):
        print("Client Sent Message")
        #Sending message to all clients
        self.broadcast(message)

    def onopen(self, client):
        print("Client Connected")

    def onclose(self, client):
        print("Client Disconnected")


def main(dat):
    server = BasicChatServer(dat)
    server.run()

dt = data.loadData()
if __name__ == "__main__":
    main(dt)