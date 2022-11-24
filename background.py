def background(threadname,path,qgn,q2,size):
    import pygame
    import time
    import os
    CarryOn=True
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    pygame.init()
    image1 = pygame.image.load(os.path.join(path,'logo.png'))
    #image1 = pygame.image.load('/home/stan/Dropbox/HM01/logo.png')
    #image1 = pygame.image.load(r"C:\Users\49176\Dropbox\HM01\logo.png")

    screen=pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    screen.fill(WHITE) 
    clock = pygame.time.Clock()
    CarryOn=True
    while True:
        time.sleep(0.1)
           
        if not q2.empty():
            if str(q2.get())=="x":
                CarryOn=True
                pygame.init()
                screen=pygame.display.set_mode(size)
                pygame.mouse.set_visible(False)
                clock=pygame.time.Clock()
        while CarryOn:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    CarryOn = False # Flag that we are done so we exit this loop
                    events = pygame.event.get()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                CarryOn=False
            screen.fill(WHITE)      
            screen.blit(image1, [(size[0]-image1.get_width())/2, (size[1]-image1.get_height())/2])            
            pygame.display.flip()
            clock.tick(10)

            if not q2.empty():
                if str(q2.get())=="y": 
                    CarryOn=False 

        pygame.display.quit()    
        pygame.quit()

