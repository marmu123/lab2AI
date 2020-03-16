class UI:
    def __init__(self, service):
        self.__service = service

    def start(self):
       self.__service.getHamiltonianCycle()
       self.__service.getPathBetweenTwoNodes()