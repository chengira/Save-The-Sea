#import your controller

import pygame

def main():
	pygame.init()
	team = {"lead": "Ira Cheng", "backend": "Chao Lin", "frontend": "Carl Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])

    #Create an instance on your controller object

    #Call your mainloop

main()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
