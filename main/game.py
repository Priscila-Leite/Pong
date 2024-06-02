import pyxel as px

class Game:

    def __init__(self):
        
        px.init(1000, 600, 'Pong')
        px.load('./game.pyxres')
        px.mouse(True)
        # Constantes
        self.const = {'radius': 15, 'width': 30, 'height': 150, 'speed': 10}

        # Inicialização dos pads --------------------------
        self.pad_left_x = self.const['width']
        self.pad_left_y = px.height/2 - self.const['height']/2
        self.pad_left_score = 0

        self.pad_right_x = px.width - self.const['width']*2
        self.pad_right_y = px.height/2 - self.const['height']/2
        self.pad_right_score = 0
        # -------------------------------------------------

        # Inicialização da bola ---------------------------
        self.ball_x = px.width/2 - 10
        self.ball_y = px.height/2 - 10
        self.ball_speed_x = self.ball_speed_y = 8
        # -------------------------------------------------

        px.run(self.update, self.draw)

    def move_pads(self):
        if px.btn(px.KEY_W):
            self.pad_left_y -= self.const['speed']
        if px.btn(px.KEY_S):
            self.pad_left_y += self.const['speed']
        if px.btn(px.KEY_UP):
            self.pad_right_y -= self.const['speed']
        if px.btn(px.KEY_DOWN):
            self.pad_right_y += self.const['speed']

        if self.pad_left_y <= 0:
            self.pad_left_y = 0
        if self.pad_left_y + 120 >= px.height:
            self.pad_left_y = px.height-120

        if self.pad_right_y <= 0:
            self.pad_right_y = 0
        if self.pad_right_y + 120 >= px.height:
            self.pad_right_y = px.height-120

    def collision_ball(self):
        # Ball x Pads -------------------------------------
        if self.ball_x - self.const['radius'] <= self.pad_left_x + self.const['width'] and self.pad_left_y <= self.ball_y <= self.pad_left_y + self.const['height']:
            self.ball_speed_x *= -1
        if self.ball_x + self.const['radius'] >= self.pad_right_x and self.pad_right_y <= self.ball_y <= self.pad_right_y + self.const['height']:
            self.ball_speed_x *= -1
        # -------------------------------------------------

        # Ball x Walls ------------------------------------
        if self.ball_x >= px.width:
            self.pad_left_score += 1
            self.ball_x = px.width/2 + self.const['radius']
            self.ball_y = px.height/2 + self.const['radius']
        if self.ball_x <= 0:
            self.pad_right_score += 1
            self.ball_x = px.width/2 + self.const['radius']
            self.ball_y = px.height/2 + self.const['radius']
        if self.ball_y >= px.height or self.ball_y <= 0:
            self.ball_speed_y *= -1
        # -------------------------------------------------
    
    def move_ball(self):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        if 0 >= self.ball_y - self.const['radius'] or self.ball_y + self.const['radius'] >= px.height:
            self.ball_speed_y *= -1

    def update(self):
        if px.btnp(px.KEY_ESCAPE):
            px.quit
        
        self.move_pads()
        self.collision_ball()
        self.move_ball()

    def draw(self):
        px.cls(14)

        px.circ(self.ball_x, self.ball_y, self.const['radius'], 8)
        px.rect(self.pad_left_x, self.pad_left_y, self.const['width'], self.const['height'], 2)
        px.rect(self.pad_right_x, self.pad_right_y, self.const['width'], self.const['height'], 2)

        # Scores
        q = len(str(self.pad_left_score))
        e = q
        for n in str(self.pad_left_score):
            px.blt(px.width/3 - q * 10 - e * 5, 20, 1, int(n)*10, 0, 10, 15, 7)
            q -= 1
            e -= 1
        q = len(str(self.pad_right_score))
        e = q
        for n in str(self.pad_right_score):
            px.blt(2*px.width/3 - q * 10 - e * 5, 20, 1, int(n)*10, 0, 10, 15, 7)
            q -= 1
            e -= 1



Game()