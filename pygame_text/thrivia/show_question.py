import pygame
import random
class Show_question():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.color = (255,255,255)
        self.r_color = (0,255,0)
        self.w_color = (255,0,0)        
        self.score = 0
        self.state = ai_game.state
        #self.current_question = 0  #控制读题数
        self.big_font = pygame.font.Font(None,60)
        self.small_font = pygame.font.Font(None,40)
        
    def show_still_font(self):  
        self.big_font_image1 = self.big_font.render("Thrivia Game",True,self.color)
        #self.big_font_image2 = self.big_font.render(f"Question {self.question_num}",True,(255,255,255))   好像可以用读取的方法来打印question n
        self.big_font_image3 = self.big_font.render("Answers",True,self.color)
        self.small_font_image1 = self.small_font.render("Press any key(1-4) to continue",True,self.color)
        self.small_font_image2 = self.small_font.render("Score",True,self.color)
        self.screen.blit(self.big_font_image1,(400,0))
        #self.screen.blit(self.big_font_image2,(0,150))
        self.screen.blit(self.big_font_image3,(0,300))
        self.screen.blit(self.small_font_image1,(350,750))
        self.screen.blit(self.small_font_image2,(900,0))
        
    def read_txt(self):
        self.file = open('amdwa.txt','r')
        self.txt_data = self.file.readlines()
        self.file.close()
        self.thrivia_data = [] #数据副本
        for data in self.txt_data:
            self.thrivia_data.append(data.strip())
            
    def show_txt(self):
        self.question_num = 0
        self.big_font_image4 = self.big_font.render(f"{self.thrivia_data[self.question_num]}",True,self.color)
        self.screen.blit(self.big_font_image4,(0,150))
        self.question_num += 1
        self.small_font_image4 = self.small_font.render(f"{self.thrivia_data[self.question_num]}",True,self.color)
        self.screen.blit(self.small_font_image4,(20,220))
        if self.state:
            for i in range(4):
              self.question_num += 1
              self.small_font_image = self.small_font.render(f"{self.thrivia_data[self.question_num]}",True,self.color)
              self.screen.blit(self.small_font_image,(20,350+40*i))
    
    def show_score(self):
        my_score = pygame.font.Font(None,40)
        my_score_image = my_score.render(f"{self.score}",True,self.color)
        self.screen.blit(my_score_image,(920,30))
        
            
    def show_answer(self):
        keys = pygame.key.get_pressed()
        showing = 0
        show_1 = 0
        show_2 = 0
        show_3 = 0
        show_4 = 0        
        if keys[pygame.K_1]:
                showing = 1
                show_1 = 1
                self.state = 0
        if keys[pygame.K_2]:   
                show_2 = 1         
                showing = 1  
                self.state = 0      
        if keys[pygame.K_3]:   
                show_3 = 1       
                showing = 1    
                self.state = 0  
        if keys[pygame.K_4]:  
                show_4 = 1
                showing = 1     
                self.state = 0       
        if not self.state:
            while showing:
                    if show_1:
                        self.small_font_image_1a = self.small_font.render(f"{self.thrivia_data[2]}",True,self.r_color)
                        self.screen.blit(self.small_font_image_1a,(20,350))
                        pygame.display.update()
                        keys = pygame.key.get_pressed()                        
                        if keys[pygame.K_KP_ENTER]:
                            showing = 0
                            show_1 = 0
                    if show_2:
                        self.small_font_image_1a = self.small_font.render(f"{self.thrivia_data[2]}",True,self.r_color)
                        self.screen.blit(self.small_font_image_1a,(20,350))   
                        self.small_font_image_2b = self.small_font.render(f"{self.thrivia_data[3]}",True,self.w_color)
                        self.screen.blit(self.small_font_image_2b,(20,390))      
                        pygame.display.update()   
                        keys = pygame.key.get_pressed()                            
                        if keys[pygame.K_RETURN]:
                            showing = 0   
                            print("1")
                            show_2 = 0             
                    if show_3:
                        self.small_font_image_1a = self.small_font.render(f"{self.thrivia_data[2]}",True,self.r_color)
                        self.screen.blit(self.small_font_image_1a,(20,350))   
                        self.small_font_image_3c = self.small_font.render(f"{self.thrivia_data[4]}",True,self.w_color)
                        self.screen.blit(self.small_font_image_3c,(20,430)) 
                        pygame.display.update()
                        keys = pygame.key.get_pressed()                      
                        if keys[pygame.K_KP_ENTER]:        #MEIAJWNDAWDOAJDJWAODALWOD???????? 
                            showing = 0    
                            show_3 = 0                                    
                    if show_4:
                        self.small_font_image_1a = self.small_font.render(f"{self.thrivia_data[2]}",True,self.r_color)
                        self.screen.blit(self.small_font_image_1a,(20,350))   
                        self.small_font_image_4d = self.small_font.render(f"{self.thrivia_data[5]}",True,self.w_color)
                        self.screen.blit(self.small_font_image_4d,(20,470))   
                        pygame.display.update()   
                        keys = pygame.key.get_pressed()                       
                        if keys[pygame.K_KP_ENTER]:
                            showing = 0  
                            show_4 = 0                                   
                        
                                        
                        
                        

                

            

        
        
            
        
        
        
        
            
        
        