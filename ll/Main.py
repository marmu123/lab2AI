from Repository import Repository
from PathFinder import PathFinder
from Service import Service
from UI import UI

repository = Repository("ll\\tsp.txt", "ll\\tsp_solution.txt")
pathFinder = PathFinder(repository)
service = Service(pathFinder)
ui = UI(service)
ui.start()
