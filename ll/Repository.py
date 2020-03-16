class Repository:
    def __init__(self, fileName, outputFileName):
        self.__fileName = fileName
        self.__outputFileName = outputFileName
        self.__startNode = 0
        self.__destinationNode = 0
        open(self.__outputFileName, 'w').close()

    def getStartNode(self):
        return self.__startNode

    def getDestinationNode(self):
        return self.__destinationNode

    def readFile(self):
        costs = []
        file = open(self.__fileName, "r")
        n = int(file.readline())
        for i in range(n):
            line = file.readline()
            costs.append(list(line.strip().split(",")))

        for row in costs:
            for i in range(len(row)):
                row[i] = int(row[i])

        self.__startNode = int(file.readline())
        self.__destinationNode = int(file.readline())
        file.close()
        return [n, costs]

    def writeFile(self, n, result, costResult):
        f = open(self.__outputFileName, "a")
        f.write(str(n) + "\n")
        string = ""
        for e in result:
            string += str(e) + " "
        f.write(string + "\n")
        f.write(str(costResult)+"\n")
        f.close()
