class Service:
    def __init__(self,pathFinder):
        self.__pathFinder=pathFinder

    def getHamiltonianCycle(self):
        aux = self.__pathFinder.getList()
        n = aux[0]
        costs = aux[1]
        visited = [0] * n
        self.__pathFinder.greedy(1, 1, costs, visited)

    def getPathBetweenTwoNodes(self):
        aux = self.__pathFinder.getList()
        n = aux[0]
        costs = aux[1]
        visited = [0] * n
        self.__pathFinder.greedy(self.__pathFinder.getStartNode(), self.__pathFinder.getDestinationNode(), costs, visited)