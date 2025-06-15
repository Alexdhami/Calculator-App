import pygame
import re

class Calc:
    def __init__(self,window,width,height):
        self.width = width
        self.height = height
        self.window = window
        self.font = pygame.font.SysFont('Arial',int(self.width*6.25/100))
        self.mouse_down = False
        self.result = "0"

    def arithmetic_operation(self,expr):
        # This is for doing expression like leading zeros except 0.x 
        final = ''

        # Spliting the expression to the mathematical symbol
        lis = re.split(r'([/\*\+\-\(\)])', expr) 

        # Note: The backslash (\) is used to escape special characters.
        # For example, the minus (-) is a range operator in regex, so we escape it to match the literal dash.
        # Similarly, parentheses are also special characters in regex (used for grouping), 
        # so we escape them to treat them as literal characters for splitting.
        # This ensures the regex splits the expression at these symbols properly.

        for i in lis:
            if not i in ['+','-','/','*']:
                if len(i)>1 and '.' not in i:
                    final += str(int(i))
                else:
                    final += i
            else:
                final += i
        return str(eval(final))
        
    def get_buttons(self,left,top,font_center,font_messege):
        button_width = self.width * 18.5/100
        button_height = self.height* 8.7 /100
        
        # Create a surface with alpha for transparency
        button = pygame.Surface((button_width,button_height),pygame.SRCALPHA)

        # Draw rounded rectangle onto the button surface
        pygame.draw.rect(button, '#0d161f', button.get_rect(), border_radius=30)
        
        # Render the text
        font_surf = self.font.render(f'{font_messege}',False,'white')
        font_rect = font_surf.get_rect(center = font_center)
        
        # Blit button onto main window
        button_rect = button.get_rect(center = (left,top))
        self.window.blit(button,button_rect)

        # Blit text onto button
        self.window.blit(font_surf,font_rect)
        
        return button_rect

    def result_box(self):
        # Draw The surface
        font = pygame.font.SysFont('Arial',int(self.width*12.5/100))
        label_surface = pygame.Surface((self.width*95/100,self.height*13/100),pygame.SRCALPHA)
        pygame.draw.rect(label_surface,'#3b6bb8',label_surface.get_rect(),border_radius=30)
        label_surface_rect = label_surface.get_rect(center = (self.width/2,self.height*25.12/100))

        messege = self.result
        max_len = 13
        if len(self.result) >max_len:
            i = len(self.result) - max_len
            messege = messege[i:]
        font_surf = font.render(f"{messege}",False,'white')

        font_rect = font_surf.get_rect(midleft = (self.width*6/100,self.height*25/100))

        self.window.blit(label_surface,label_surface_rect)
        self.window.blit(font_surf,font_rect)

    def screening_all(self,mouse_pos):
        self.result_box()
        
        button_0 = self.get_buttons(self.width* 14.25/100,self.height * 91.3/100,(self.width* 14.25/100,self.height * 91.3/100),0)
        button_dot = self.get_buttons(self.width* 37.25/100,self.height * 91.3/100,(self.width* 37.25/100,self.height * 91.3/100),'.')
        button_percentage = self.get_buttons(self.width* 61/100,self.height * 91.3/100,   (self.width* 61/100,   self.height * 91.3/100),'%')
        button_plus = self.get_buttons(self.width* 84.25/100,self.height * 91.3/100,(self.width* 84.25/100,self.height * 91.3/100),'+')

        button_1 = self.get_buttons(self.width* 14.25/100,self.height * 80.6/100,(self.width* 14.25/100,self.height * 80.6/100),1)
        button_2 = self.get_buttons(self.width* 37.25/100,self.height * 80.6/100,(self.width* 37.25/100,self.height * 80.6/100),2)
        button_3 = self.get_buttons(self.width* 61/100,self.height * 80.6/100,   (self.width* 61/100,   self.height * 80.6/100),3)
        button_minus = self.get_buttons(self.width* 84.25/100,self.height * 80.6/100,(self.width* 84.25/100,self.height * 80.6/100),'-')
        
        button_4 = self.get_buttons(self.width* 14.25/100,self.height * 69.9/100,(self.width* 14.25/100,self.height * 69.9/100),4)
        button_5 = self.get_buttons(self.width* 37.25/100,self.height * 69.9/100,(self.width* 37.25/100,self.height * 69.9/100),5)
        button_6 = self.get_buttons(self.width* 61/100,self.height * 69.9/100,   (self.width* 61/100,   self.height * 69.9/100),6)
        button_multi = self.get_buttons(self.width* 84.25/100,self.height * 69.9/100,(self.width* 84.25/100,self.height *69.9/100),'x')

        button_7 = self.get_buttons(self.width* 14.25/100,self.height * 59.2/100,(self.width* 14.25/100,self.height * 59.2/100),7)
        button_8 = self.get_buttons(self.width* 37.25/100,self.height * 59.2/100,(self.width* 37.25/100,self.height * 59.2/100),8)
        button_9 = self.get_buttons(self.width* 61/100,self.height * 59.2/100,   (self.width* 61/100,   self.height * 59.2/100),9)
        button_devide = self.get_buttons(self.width* 84.25/100,self.height * 59.2/100,(self.width* 84.25/100,self.height *59.2/100),'/')

        button_remove = self.get_buttons(self.width* 14.25/100,self.height * 48.5/100,(self.width* 14.25/100,self.height * 48.5/100),'C')
        button_left_braces = self.get_buttons(self.width* 37.25/100,self.height * 48.5/100,(self.width* 37.25/100,self.height * 48.5/100),'(')
        button_right_braces = self.get_buttons(self.width* 61/100,self.height * 48.5/100,   (self.width* 61/100,   self.height * 48.5/100),')')
        button_equals = self.get_buttons(self.width* 84.25/100,self.height * 48.5/100,(self.width* 84.25/100,self.height *48.5/100),'=')
        
        if button_0.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0':
                    self.result = '0'
                else:
                    self.result += '0'
                self.mouse_down = False
        if button_1.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '1'
                else:
                    self.result += '1'
                self.mouse_down = False
        if button_2.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '2'
                else:
                    self.result += '2'
                self.mouse_down = False
        if button_3.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '3'
                else:
                    self.result += '3'
                self.mouse_down = False
        if button_4.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '4'
                else:
                    self.result += '4'
                self.mouse_down = False
        if button_5.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '5'
                else:
                    self.result += '5'
                self.mouse_down = False
        if button_6.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '6'
                else:
                    self.result += '6'
                self.mouse_down = False
        if button_7.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '7'
                else:
                    self.result += '7'
                self.mouse_down = False
        if button_8.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '8'
                else:
                    self.result += '8'
                self.mouse_down = False
        if button_9.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '9'
                else:
                    self.result += '9'
                self.mouse_down = False
        if button_left_braces.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == '0' or self.result == 'Error':
                    self.result = '('
                else:
                    self.result += '('
                self.mouse_down = False
        if button_right_braces.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = ')'
                else:

                    self.result += ')'
                self.mouse_down = False
        if button_remove.collidepoint(mouse_pos):
            if self.mouse_down:

                self.result = '0'
                self.mouse_down = False
        if button_dot.collidepoint(mouse_pos):
            if self.mouse_down:
                if not self.result:
                    self.result += '0.'
                else:
                    if self.result == 'Error':
                        self.result = '0.'
                    else:
                        self.result += '.'
                self.mouse_down = False
        if button_percentage.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = '0%'
                else:
                    self.result += '%'
                self.mouse_down = False
        if button_plus.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = '0+'
                else:
                    self.result += '+'
                self.mouse_down = False
        if button_minus.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = '0-'
                else:
                    self.result += '-'
                self.mouse_down = False
        if button_multi.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = '0x'
                else:
                    self.result += 'x'
                self.mouse_down = False
        if button_devide.collidepoint(mouse_pos):
            if self.mouse_down:
                if self.result == 'Error':
                    self.result = '0/'
                else:
                    self.result += '/'
                self.mouse_down = False   
        if button_equals.collidepoint(mouse_pos):
            if self.mouse_down:
                try:
                    expression = self.result.replace('x', '*').replace('%', '/100')
                    result = float(self.arithmetic_operation(expression))

                    # Fix floating point display error (like 0.1 + 0.2)
                    rounded_result = round(result, 10)  # Round to avoid long float errors
                    result_str = str(rounded_result)
                    if rounded_result.is_integer():
                        result_str = str(int(rounded_result))
                    else:
                        result_str = str(rounded_result)

                    # Check if it's too long for display
                    if len(result_str) > 9:
                        self.result = f'{rounded_result:.6e}'  # scientific notation
                    else:
                        self.result = result_str

                except Exception as e:
                    self.result = 'Error'

                self.mouse_down = False


def button_press(event,calc):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                if calc.result == '0':
                    calc.result = '0'
                else:
                    if calc.result == 'Error':
                        calc.result = '0'
                    else:
                        calc.result += '0'
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                if calc.result == '0':
                    calc.result = '1'
                else:
                    if calc.result == 'Error':
                        calc.result = '1'
                    else:
                        calc.result += '1'
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                if calc.result == '0':
                    calc.result = '2'
                else:
                    if calc.result == 'Error':
                        calc.result = '2'
                    else:
                        calc.result += '2'
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                if calc.result == '0':
                    calc.result = '3'
                else:
                    if calc.result == 'Error':
                        calc.result = '3'
                    else:
                        calc.result += '3'
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                if calc.result == '0':
                    calc.result = '4'
                else:
                    if calc.result == 'Error':
                        calc.result = '4'
                    else:
                        calc.result += '4'
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                if calc.result == '0':
                    calc.result = '5'
                else:
                    if calc.result == 'Error':
                        calc.result = '5'
                    else:
                        calc.result += '5'
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                if calc.result == '0':
                    calc.result = '6'
                else:
                    if calc.result == 'Error':
                        calc.result = '6'
                    else:
                        calc.result += '6'
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                if calc.result == '0':
                    calc.result = '7'
                else:
                    if calc.result == 'Error':
                        calc.result = '7'
                    else:
                        calc.result += '7'
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                if calc.result == '0':
                    calc.result = '8'
                else:
                    if calc.result == 'Error':
                        calc.result = '8'
                    else:
                        calc.result += '8'
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                if calc.result == '0':
                    calc.result = '9'
                else:
                    if calc.result == 'Error':
                        calc.result = '9'
                    else:
                        calc.result += '9'
            if event.key == pygame.K_RETURN or event.key == pygame.K_EQUALS or event.key == pygame.K_KP_ENTER:
                try:
                    expression = calc.result.replace('x', '*').replace('%', '/100')

                    result = float(calc.arithmetic_operation(expression))
                    result_str = str(result)

                    if len(result_str) > 9:
                        calc.result = f'{result:.6e}'  # scientific notation
                    else:
                        calc.result = result_str
                except:
                    calc.result = 'Error'

            if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                if calc.result == '0':
                    calc.result = '0.'
                else:
                    if calc.result == 'Error':
                        calc.result = '0.'
                    else:
                        calc.result += '.'
            
            if event.key == pygame.K_PERCENT:    
                if calc.result == 'Error':
                        calc.result = '0%'
                else:
                    calc.result += '%'

            if event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT or event.key == pygame.K_KP_PLUS:
                if calc.result == 'Error':
                        calc.result = '0+'
                else:
                    calc.result += '+'
      
            if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if calc.result == 'Error':
                        calc.result = '0-'
                else:
                    calc.result += '-'

            if event.key == pygame.K_ASTERISK or event.key == pygame.K_KP_MULTIPLY:
                if calc.result == 'Error':
                        calc.result = '0x'
                else:
                    calc.result += 'x'

            if event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
                if calc.result == 'Error':
                        calc.result = '0/'
                else:
                    calc.result += '/'

            if event.key == pygame.K_BACKSPACE:

                if calc.result == 'Error':
                    calc.result = '0'
                else:
                    calc.result = calc.result[:-1]
                    if len(calc.result)==0:
                        calc.result = '0'
