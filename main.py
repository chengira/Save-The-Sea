#import your controller

import pygame
from src import controller 
def main():
	pygame.init()
	team = {"lead": "Ira Cheng", "backend": "Carl Huang", "frontend": "Chao Lin"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
	main_window = controller.Controller()
	main_window.mainLoop()

    #Create an instance on your controller object

    #Call your mainloop

main()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
