import pygame
from GameField import *

class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
        self.__game_field = None
        
        self.CELL_WIDTH = 10
        self.INDENT = 4 * self.CELL_WIDTH
        self.colors = {
            "BLACK" : (0, 0, 0),
            "WHITE" : (255, 255, 255),
            "RED" : (255, 0, 0)
            }

        pygame.init()
        self.__screen = pygame.display.set_mode((width, height))
        self.__text_font = pygame.font.Font("font\kenpixel_mini_square.ttf", 20)
        
        pygame.display.set_caption("Snake game")
        self.__screen.fill(self.colors["WHITE"])
        
    def draw(self):
        self.__screen.fill(self.colors["WHITE"])
        
        self.draw_game_field()
        
        text_score = self.__text_font.render(str(self.__game_field.score), 0, self.colors["BLACK"])
        self.__screen.blit(text_score, (self.CELL_WIDTH, self.CELL_WIDTH))

        pygame.display.update()

    def draw_game_field(self):       
        left = self.__game_field.left_edge * self.CELL_WIDTH
        right = self.__game_field.right_edge * self.CELL_WIDTH
        top = self.__game_field.top_edge * self.CELL_WIDTH
        bot = self.__game_field.bot_edge * self.CELL_WIDTH

        # Top edge
        pygame.draw.line(self.__screen, self.colors["BLACK"], (left, top),
                         (right, top))
        # Bottom edge
        pygame.draw.line(self.__screen, self.colors["BLACK"], (left, bot),
                         (right, bot))
        # Right edge
        pygame.draw.line(self.__screen, self.colors["BLACK"], (right, top),
                         (right, bot))
        # Left edge
        pygame.draw.line(self.__screen, self.colors["BLACK"], (left, top),
                         (left, bot))

 

    def set_game_field(self):
        if self.__game_field is None:
            edges = self.INDENT, self.__width - self.INDENT, self.INDENT, self.__width - self.INDENT
            edges = [i // self.CELL_WIDTH for i in edges]

            self.__game_field = GameField(*edges)

        return self.__game_field

def main():
    width = 500
    win = Window(width, width)
    
    game_field = win.set_game_field()

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()       

        win.draw()


if __name__ == '__main__':
    main()
