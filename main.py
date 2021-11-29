#import your controller

import pygame
import controller
def main():
	pygame.init()
	team = {"lead": "Ira Cheng", "backend": "Chao Lin", "frontend": "Carl Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
	main_window = controller.Controller()
	main_window.mainLoop()

    #Create an instance on your controller object

    #Call your mainloop

main()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
