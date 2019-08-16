import pygame

from GameField import GameField

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
        self.draw_snake()
        self.draw_food()
        
        # Draw score
        text_score = self.__text_font.render(str(self.__game_field.score), 0, self.colors["BLACK"])
        self.__screen.blit(text_score, (self.CELL_WIDTH * 2, self.CELL_WIDTH))

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

    def draw_snake(self):
        snake = self.__game_field.snake
        if snake is not None:
            for i in snake:
                pygame.draw.rect(self.__screen, self.colors["BLACK"], [i.x * self.CELL_WIDTH,
                                 i.y * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH])

    def draw_food(self):
        food = self.__game_field.food
        if food is not None:           
            pygame.draw.rect(self.__screen, self.colors["RED"], [food.x * self.CELL_WIDTH,
                             food.y * self.CELL_WIDTH, self.CELL_WIDTH, self.CELL_WIDTH])

    def add_game_field(self):
        if self.__game_field is None:
            edges = (self.INDENT, self.__width - self.INDENT,
                     self.INDENT, self.__width - self.INDENT)
            edges = [i // self.CELL_WIDTH for i in edges]

            self.__game_field = GameField(*edges)

        return self.__game_field

    # Main menu loop
    def main_menu(self):
        first_but_pos = (self.__width // 2,
                         self.__height // 2 - 2 * self.INDENT)
        
        buttons = [pygame.image.load('buttons/Play_but.png'),
                   pygame.image.load('buttons/Play_but_on.png')]

        self.__screen.fill(self.colors["WHITE"])
        
        while True:
            play_button = buttons[0]
            
            rect = play_button.get_rect(center = first_but_pos)

            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
                # Start game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and rect.collidepoint(mouse_position):
                        self.game_loop()
                        return

            # On play button
            if rect.collidepoint(mouse_position):
                play_button = buttons[1]
            
            self.__screen.blit(play_button, (rect.x, rect.y))

            pygame.display.update()
    
    # Main game loop
    def game_loop(self):
        snake = self.__game_field.add_snake()
    
        clock = pygame.time.Clock()

        while True:
            pygame.time.delay(50)
            clock.tick(12)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()       
        
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    snake.change_direction('left')
                    break
            
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    snake.change_direction('right')
                    break
            
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    snake.change_direction('up')
                    break
            
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    snake.change_direction('down')
                    break
        

            if self.__game_field.food is None:
               self.__game_field.add_food()
        
            if not snake.move():
                break
        
            self.draw()


def main():
    width = 500
    win = Window(width, width)
    win.add_game_field()
    
    win.main_menu()

    


if __name__ == '__main__':
    main()
