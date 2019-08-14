from GameFieldObject import GameFieldObject

class SnakeBody(GameFieldObject):
    def __init__(self, x, y):
        return super().__init__(x, y)

class Snake():
    def __init__(self, x, y, game_field):
        self.__game_field = game_field
        
        self.__head = SnakeBody(x, y)
        self.__body = [self.__head, SnakeBody(x + 1, y), SnakeBody(x + 2, y), SnakeBody(x + 3, y), SnakeBody(x + 4, y)]
        self.__directions = [(-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0)]

    def __iter__(self):
        for i in self.__body:
            yield i

    def __contains__(self, other):
        coordinates = [(i.x, i.y) for i in self.__body]
        return other in coordinates

    def move(self):
        left = self.__game_field.left_edge 
        right = self.__game_field.right_edge 
        top = self.__game_field.top_edge 
        bot = self.__game_field.bot_edge 
        
        for i in range(len(self.__body)):
            self.__body[i].x += self.__directions[i][0]
            self.__body[i].y += self.__directions[i][1]

            # Check edges of game field
            # Left edge
            if self.__body[i].x < left:
                self.__body[i].x = right - 1
            # Right edge
            elif self.__body[i].x > right - 1:
                self.__body[i].x = left
            # Top edge
            if self.__body[i].y < top:
                self.__body[i].y = bot - 1
            # Bottom edge
            elif self.__body[i].y > bot - 1:
                self.__body[i].y = top
        
        # Offset directions for body
        x, y = self.__directions[0][0], self.__directions[0][1]
        self.__directions.insert(0, (x, y))
        self.__directions.pop()

    def change_direction(self, direction : str):
        dir = {
            "left" : (-1, 0), "right" : (1, 0),
            "up" : (0, -1), "down" : (0, 1)
        }

        dx = self.__directions[0][0]
        dy = self.__directions[0][1]

        if (dir[direction.lower()][0] != -dx and
                dir[direction.lower()][1] != -dy):
            self.__directions[0] = dir[direction.lower()]




