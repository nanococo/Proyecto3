import copy


def loadCountries():
    # Loads countries file and add country to a list
    countriesFile = open("dataFiles/Paises.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").split(";", ) for line in countriesFile.readlines() if line.strip()]
    keysList = []
    final = []

    for i in splitList:
        if len(i) == 2:
            if i[0] not in keysList:
                keysList.append(i[0])
                final.append(i)

    # print(keysList)
    # print(final)

    return final


def loadCities():
    # Loads cities file and add cities to a list
    countriesFile = open("dataFiles/Ciudades.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").strip().split(";", ) for line in countriesFile.readlines() if line.strip()]
    keysList = []
    final = []

    for i in splitList:
        if len(i) == 3:
            if i[1] not in keysList:
                keysList.append(i[1])
                final.append(i)

    # print(final)
    # print(keysList)

    return final


def getConnectionByIdWithStandAloneConnection(connectionList, find):
    # Looks for a specific connection by its ID
    found = []
    for i in connectionList:
        if i[2] == find:
            found = i
            break

    return found



def countryAndCityExistInList(country, city, providedList):
    # Looks for the country and city to exist on a given list
    found = False
    for i in range(len(providedList)):
        for j in range(len(providedList[i][2])):
            if providedList[i][0] == country and providedList[i][2][j][0] == city:
                found = True
    return found


def countryExistsInList(countryCode, providedList):
    # Look only for country on given list
    """Looks if a country exists within the lists"""

    found = False
    for i in providedList:
        if i[0] == countryCode:
            found = True
    return found


def loadConnections(countryCityList):
    # Loads connections file and add connections to a list
    countryForConn = copy.deepcopy(countryCityList)

    countriesFile = open("dataFiles/Conexiones.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").strip().split(";", ) for line in countriesFile.readlines() if line.strip()]
    keysList = []
    final = []
    for i in range(len(splitList)):
        if len(splitList[i]) == 6:
            if countryAndCityExistInList(splitList[i][0], splitList[i][1], countryForConn) and countryAndCityExistInList(splitList[i][3], splitList[i][4], countryForConn):
                if splitList[i][2] not in keysList:
                    keysList.append(splitList[i][2])
                    final.append(splitList[i])

    return final


def loadRoutes():
    # Loads routes file and add routes to a list
    countriesFile = open("dataFiles/Rutas.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").strip().split(";", ) for line in countriesFile.readlines() if line.strip()]
    final = []
    for i in splitList:
        if len(i) == 7:
            if i not in final and i[6].isdigit():
                final.append(i)

    return final


def loadUsers():
    # Loads users file and add users to a list
    countriesFile = open("dataFiles/Usuarios.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").strip().split(";", ) for line in countriesFile.readlines() if line.strip()]
    keysList = []
    final = []

    for i in splitList:
        if len(i) == 5:
            if i[2] not in keysList:
                keysList.append(i[2])
                if i[4] == "0" or i[4] == "1":
                    final.append(i)

    return final


def loadAdmins():
    # Loads admins file and add admins to a list
    countriesFile = open("dataFiles/Administradores.txt", 'r', encoding='utf-8')
    splitList = [line.replace("\n", "").split(";", ) for line in countriesFile.readlines() if line.strip()]
    keysList = []
    final = []

    for i in splitList:
        if len(i) == 2:
            if i[0] not in keysList:
                keysList.append(i[0])
                final.append(i)

    return final


def mergeCountryCity(countriesList, citiesList):
    # Merges the country list with the city list
    final = countriesList

    for i in range(len(countriesList)):
        key = countriesList[i][0]
        citiesForCountry = []

        for j in citiesList:
            if j[0] == key:
                citiesForCountry.append(j[1:])

        # print(citiesForCountry)
        final[i].append(citiesForCountry)

    return final


def connectionExists(depCoun, depCity, arrivCoun, arrivCity, listOfConnections):
    # Returns true or false if connections exists
    found = False
    for i in listOfConnections:
        if i[0] == depCoun and i[1] == depCity and i[3] == arrivCoun and i[4] == arrivCity:
            found = True
    return found


def mergeTrainRoute(trainsList, routesList, connectionsListForMerge):
    # Merges the Train list with the Route List
    final = trainsList

    for i in range(len(trainsList)):
        routesForTrains = []
        key = trainsList[i][1]

        for j in routesList:
            if j[1] == key:
                if connectionExists(j[2], j[3], j[4], j[5], connectionsListForMerge) and trainsList[i][4] == j[2] and trainsList[i][5] == j[3]:
                    routesForTrains.append(j[2:])

        final[i].append(routesForTrains)
    return final


class loadData:

    def getConnectionById(self, fullConnectionList, connectionId):
        foundConnections = []
        for i in fullConnectionList:
            for j in i[2]:
                for k in j[2]:
                    if k[0] == connectionId:
                        foundConnections.append([i[0], j[0]] + k)
        return foundConnections

    def connectionFullExists(self, departCountry, departCity, arriveCountry, arriveCity):
        # Checks if connection exist with given params
        found = False
        for i in self.countryCitiesConnections:
            if i[0] == departCountry:
                for j in i[2]:
                    if j[0] == departCity:
                        for k in j[2]:
                            if k[1] == arriveCountry and k[2] == arriveCity:
                                found = True
        return found

    def getConnectionId(self, departCountry, departCity, arriveCountry, arriveCity):
        ConnId = "null"
        for i in self.countryCitiesConnections:
            if i[0] == departCountry:
                for j in i[2]:
                    if j[0] == departCity:
                        for k in j[2]:
                            if k[1] == arriveCountry and k[2] == arriveCity:
                                ConnId = k[0]
        return ConnId


    def loadTrains(self):
        # Loads trains file and add trains to a list
        countriesFile = open("dataFiles/Trenes.txt", 'r', encoding='utf-8')
        splitList = [line.replace("\n", "").strip().split(";", ) for line in countriesFile.readlines() if line.strip()]
        keysList = []
        final = []

        for i in splitList:
            if len(i) == 6:
                if i[0] in self.trainTypes:
                    if [i[0], i[1]] not in keysList and i[0].isdigit() and i[3].isdigit():
                        if countryAndCityExistInList(i[4], i[5], self.countryCitiesConnections):
                            keysList.append([i[0], i[1]])
                            final.append(i)

        return final

    # Merges the CountryCity lst with the Connections
    def mergeCountryCityConnections(self, countryCity, connectionsCopyList):
        final = copy.deepcopy(self.countryCities)
        for i in range(len(countryCity)):
            countryKey = countryCity[i][0]
            connectionsToAdd = []

            for j in range(len(countryCity[i][2])):
                cityKey = countryCity[i][2][j][0]
                for k in connectionsCopyList:
                    if k[0] == countryKey and k[1] == cityKey:
                        connectionsToAdd.append(k[2:])

                final[i][2][j].append(connectionsToAdd)

        return final



#REPORTING METHODS
    def initialize(self, trainRoutes, countryCitiesConnections, users):
        # Trains and routes
        for i in trainRoutes:
            self.trainsByUsage.append([i[:3], 0])

            if i[6]:
                self.routesByUsage.append([i[:3] + i[6][0][:4], 0])

        # Cities and country
        for i in countryCitiesConnections:
            self.countriesByUsage.append([i[:2], 0])

            for j in range(len(i[2])):
                self.citiesByUsage.append([[i[0], i[2][j][:2]], 0])

        # Users
        for i in users:
            self.usersByUsage.append([i[2:4], 0])

    def addUserTravelCount(self, user, trips):
        for i in self.usersByUsage:
            if i[0][1] == user:
                i[1] += trips

    def addCityCount(self, country, city):
        for i in self.citiesByUsage:
            if i[0][0] == country and i[0][1][0] == city:
                i[1] += 1

    def addCountryCount(self, country):
        for i in self.countriesByUsage:
            if i[0][0] == country:
                i[1] += 1

    def addRoutesCount(self, trainTypeCode, trainCode, departCountry, departCity, arriveCity, arriveCountry):
        for i in self.routesByUsage:
            if i[0][0] == trainTypeCode and i[0][1] == trainCode and i[0][3] == departCountry and i[0][4] == departCity and i[0][5] == arriveCity and i[0][6] == arriveCountry:
                i[1] += 1

    def addTrainCount(self, trainType, trainCode):
        for i in self.trainsByUsage:
            if i[0][0] == trainType and i[0][1] == trainCode:
                i[1] += 1

    def deleteCountryReports(self, countryCode):
        """Returns a list without the desired countries"""
        newCityList = []
        for i in self.countriesByUsage:
            if not i[0][0] == countryCode:
                newCityList.append(i)
        return newCityList

    def deleteCityReports(self, countryCodem, cityCode):
        """Returns a list without the desired cities"""
        newList = []
        for i in self.citiesByUsage:
            if not (i[0][0] == countryCodem and i[0][1][0] == cityCode):
                newList.append(i[0])
        return newList

    def deleteRoutesReport(self, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity, newRouteArrivalCountry, newRouteArrivalCity):
        """Returns a list without the desired connections"""
        newList = []
        for i in self.routesByUsage:
            if not (i[0] == newRouteTrainType and i[1] == newRouteTrainCode and i[3] == newRouteDepartCountry and i[4] == newRouteDepartCity and i[5] == newRouteArrivalCountry and i[6] == newRouteArrivalCity):
                newList.append(i)
        return newList

    def deleteTrainForReports(self, trainType, trainCode):
        """Returns a list without the desired trains"""
        newList = []
        for i in self.trainsByUsage:
            if not (i[0][0] == trainType and i[0][1] == trainCode):
                newList.append(i)
        return newList

####################################################################################333
    def getMostUsedRoute(self):
        """Prints routes with the highest usage"""
        returnList = []
        comp = 0
        for i in self.routesByUsage:
            if i[1] > comp:
                comp = i[1]
        for i in self.routesByUsage:
            if i[1] == comp:
                returnList.append("Train type: " + i[0][0] + ". Train Code: " + i[0][1] + ". Name: " + i[0][2] + ". Depart: " + i[0][3] + ", " + i[0][4] + ". Arrive: " + i[0][5] + ", " + i[0][6] + ". Uses:" + str(i[1]))
        return returnList

    def getLeastUsedRoute(self):
        """Prints routes with the lowest usage"""
        returnList = []
        comp = 0
        for i in self.routesByUsage:
            comp = i[1]
            if i[1] < comp:
                comp = i[1]
        for i in self.routesByUsage:
            if i[1] == comp:
                returnList.append("Train type: " + i[0][0] + ". Train Code: " + i[0][1] + ". Name: " + i[0][2] + ". Depart: " + i[0][3] + ", " + i[0][4] + ". Arrive: " + i[0][5] + ", " + i[0][6] + ". Uses:" + str(i[1]))
        return returnList

    def getMostVisitedCountry(self):
        """Prints country with the highest usage"""
        returnList = []
        comp = 0
        for i in self.countriesByUsage:
            if i[1] > comp:
                comp = i[1]
        for i in self.countriesByUsage:
            if i[1] == comp:
                returnList.append("Country: " + i[0][0] + ", " + i[0][1] + ". Uses: " + str(i[1]))
        return returnList

    def getMostVisitedCity(self):
        """Prints country with the highest usage"""
        returnList = []
        comp = 0
        for i in self.citiesByUsage:
            if i[1] > comp:
                comp = i[1]
        for i in self.citiesByUsage:
            if i[1] == comp:
                returnList.append("Country: " + i[0][0] + ", City: " + i[0][1][0] + ", " + i[0][1][1] + ". Uses: " + str(i[1]))
        return returnList

    def getHighestUsageUser(self):
        """Prints country with the highest usage"""
        returnList = []
        comp = 0
        for i in self.usersByUsage:
            if i[1] > comp:
                comp = i[1]
        for i in self.usersByUsage:
            if i[1] == comp:
                returnList.append("User ID: " + i[0][0] + ". Name: " + i[0][1] + ". Uses: " + str(i[1]))
        return returnList

    def getLeastUsageUser(self):
        """Prints routes with the lowest usage"""
        returnList = []
        comp = 0
        for i in self.usersByUsage:
            comp = i[1]
            if i[1] < comp:
                comp = i[1]
        for i in self.usersByUsage:
            if i[1] == comp:
                returnList.append("User ID: " + i[0][0] + ". Name: " + i[0][1] + ". Uses: " + str(i[1]))
        return returnList

    def getUserPurchases(self, userId):
        """Prints user purchases from given user"""
        returnList = []
        for i in self.usersByUsage:
            if i[0][1] == userId:
                returnList.append("Purchases: " + str(i[1]))
        return returnList

    def getHighestUsageTrain(self):
        """Prints train with the highest usage"""
        returnList = []
        comp = 0
        for i in self.trainsByUsage:
            if i[1] > comp:
                comp = i[1]
        for i in self.trainsByUsage:
            if i[1] == comp:
                returnList.append("Train type: " + i[0][0] + ". Train Code: " + i[0][1] + ". Name: " + i[0][2] + ". Uses: " + str(i[1]))
        return returnList

    def getLowestUsageTrain(self):
        """Prints trains with the lowest usage"""
        returnList = []
        comp = 0
        for i in self.trainsByUsage:
            comp = i[1]
            if i[1] < comp:
                comp = i[1]
        for i in self.trainsByUsage:
            if i[1] == comp:
                returnList.append("Train type: " + i[0][0] + ". Train Code: " + i[0][1] + ". Name: " + i[0][2] + ". Uses: " + str(i[1]))
        return returnList

    def reduceSeatsBy(self, num, trainType, trainCode):
        for i in self.trainRoutes:
            if i[0] == trainType and i[1] == trainCode:
                seats = int(i[3])
                seats -= num
                i[3] = str(seats)

    def __init__(self):
        self.trainTypes = ['01', '02', '03', '04']
        # Initialization of stand alone lists
        self.countries = loadCountries()
        self.cities = loadCities()

        self.routes = loadRoutes()
        self.users = loadUsers()
        self.admin = loadAdmins()

        # Copying of variables for merging purpose
        self.countriesCopy = copy.deepcopy(self.countries)
        self.citiesCopy = copy.deepcopy(self.cities)
        self.routesCopy = copy.deepcopy(self.routes)

        # Merging the Cities
        self.countryCities = mergeCountryCity(self.countriesCopy, self.citiesCopy)

        # Connections are done at the end because they require previous merged lists
        self.connections = loadConnections(self.countryCities)
        self.connectionsCopy = copy.deepcopy(self.connections)
        self.connectionsCopyForRoutes = copy.deepcopy(self.connections)
        self.countryCitiesConnections = self.mergeCountryCityConnections(self.countryCities, self.connectionsCopy)

        # Merging the routes and trains
        self.trains = self.loadTrains()
        self.trainsCopy = copy.deepcopy(self.trains)
        self.trainRoutes = mergeTrainRoute(self.trainsCopy, self.routesCopy, self.connectionsCopyForRoutes)

        # Copies for Reports
        self.countriesReports = copy.deepcopy(self.countries)
        self.routesReports = copy.deepcopy(self.routes)
        self.citiesReports = copy.deepcopy(self.cities)
        self.userReports = copy.deepcopy(self.users)
        self.trainsReports = copy.deepcopy(self.trains)

        # For usage logic
        self.routesByUsage = []
        self.trainsByUsage = []
        self.usersByUsage = []
        self.countriesByUsage = []
        self.citiesByUsage = []

        # Last Inserted Values
        self.lastCountryInsert = []
        self.lastCityInsert = []
        self.lastConnectionInsert = []
        self.lastTrainInsert = []
        self.lastRouteInsert = []
        self.lastDeletedTrain = []
        self.lastDeletedRoute = []

        # Initialize Reports
        self.initialize(self.trainRoutes, self.countryCitiesConnections, self.users)

        # print("Connections: ", self.countryCitiesConnections)
        # print("TrainRoutes:", self.trainRoutes)
