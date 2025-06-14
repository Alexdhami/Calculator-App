import pygame 
import calculator
pygame.init()

width = 500
height = width * 155/100
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Calculator')
fps = 60
clock = pygame.time.Clock()
            
calc = calculator.Calc(window,width,height)
while True:
    window.fill('#1D1E26')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                calc.mouse_down = True
      
        calculator.button_press(event,calc)

    mouse_pos = pygame.mouse.get_pos()
    calc.calculations(mouse_pos)
    
    pygame.display.update()
    clock.tick(fps)