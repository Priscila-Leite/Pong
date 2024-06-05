import pyxel as px

# Adicionar opção de 1 ou 2 players
class Game():

    def __init__(self, players):
        self.pause = True
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
        if self.pad_left_y + self.const['height'] >= px.height:
            self.pad_left_y = px.height-self.const['height']

        if self.pad_right_y <= 0:
            self.pad_right_y = 0
        if self.pad_right_y + self.const['height'] >= px.height:
            self.pad_right_y = px.height-self.const['height']

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
            self.pause = True
        if self.ball_x <= 0:
            self.pad_right_score += 1
            self.ball_x = px.width/2 + self.const['radius']
            self.ball_y = px.height/2 + self.const['radius']
            self.pause = True
        if self.ball_y >= px.height or self.ball_y <= 0:
            self.ball_speed_y *= -1
        # -------------------------------------------------
    
    def move_ball(self):
        if self.pause:
            return
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        if 0 >= self.ball_y - self.const['radius'] or self.ball_y + self.const['radius'] >= px.height:
            self.ball_speed_y *= -1

    def update_game(self):
        if px.btnp(px.KEY_SPACE):
            self.pause = not self.pause
        
        self.move_pads()
        self.collision_ball()
        self.move_ball()

    def draw_game(self):
        px.cls(14)

        px.circ(self.ball_x, self.ball_y, self.const['radius'], 2)
        px.rect(self.pad_left_x, self.pad_left_y, self.const['width'], self.const['height'], 8)
        px.rect(self.pad_right_x, self.pad_right_y, self.const['width'], self.const['height'], 8)

        # Scores
        px.text(20, 20, "Texto normal", 7)
        px.text(20, 40, "Texto escalado", 7)
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
