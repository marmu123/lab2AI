class PathFinder:
    def __init__(self, repository):
        self.__repository = repository


    def getList(self):
        return self.__repository.readFile()

    def getStartNode(self):
        return self.__repository.getStartNode()

    def getDestinationNode(self):
        return self.__repository.getDestinationNode()

    def getMax(self,list):
        return max(list)


    def getNextNode(self, list, visited):
        node = 0
        min = self.getMax(list)
        for i in range(len(list)):
            if list[i] <= min and visited[i] == 0:
                min = list[i]
                node = i + 1
        return node


    def allNodesHaveBeenVisited(self,visited):
        for e in visited:
            if e == 0:
                return False
        return True



    def greedy(self, startNode, destinationNode, costs, visited):
        result = []
        currentNode = startNode
        rez = 0

        while (not self.allNodesHaveBeenVisited(visited)):

            visited[currentNode - 1] = 1
            result.append(currentNode)
            nextNode = self.getNextNode(costs[currentNode - 1], visited)
            rez += costs[currentNode - 1][nextNode - 1]
            currentNode = nextNode
            if currentNode == destinationNode:
                break

        if self.allNodesHaveBeenVisited(visited) and destinationNode == startNode:
            rez += costs[currentNode - 1][startNode - 1]

        if startNode != destinationNode:
            result.append(destinationNode)
        self.__repository.writeFile(len(result), result, rez)
