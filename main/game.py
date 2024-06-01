import pyxel as px


class Game:
    '''
    CLASSE DO JOGO PONG

    Constantes:
    - Medidas dos pads: 25 x 120
    - Raio da bola: 10

    Pyxres:
    - Bola: (0,0)
    - Pad: (25, 0)
    '''
    def __init__(self):
        
        px.init(1000, 600, 'Pong')
        px.load('./game.pyxres')
        px.mouse(True)


        # Inicialização dos pads --------------------------
        self.pad_left_x = 20
        self.pad_left_y = px.height/2 - 40
        self.pad_right_x = px.width - 40
        self.pad_right_y = px.height/2 - 40
        self.pads_speed = 5
        # -------------------------------------------------

        # Inicialização da bola ---------------------------
        self.ball_x = px.width/2 - 10
        self.ball_y = px.height/2 - 10
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        # -------------------------------------------------

        px.run(self.update, self.draw)

    def move_pads(self):
        if px.btn(px.KEY_W):
            self.pad_left_y -= self.pads_speed
        if px.btn(px.KEY_S):
            self.pad_left_y += self.pads_speed
        if px.btn(px.KEY_UP):
            self.pad_right_y -= self.pads_speed
        if px.btn(px.KEY_DOWN):
            self.pad_right_y += self.pads_speed

        if self.pad_left_y <= 0:
            self.pad_left_y = 0
        if self.pad_left_y + 120 >= px.height:
            self.pad_left_y = px.height-120

        if self.pad_right_y <= 0:
            self.pad_right_y = 0
        if self.pad_right_y + 120 >= px.height:
            self.pad_right_y = px.height-120

    def update(self):
        if px.btnp(px.KEY_ESCAPE):
            px.quit
        
        self.move_pads()

    def draw(self):
        px.cls(0)

        px.blt(self.ball_x, self.ball_y, 0, 0, 0, 20, 20, 0)
        px.blt(self.pad_left_x, self.pad_left_y, 0, 25, 0, 25, 120)
        px.blt(self.pad_right_x, self.pad_right_y, 0, 25, 0, 25, 120)



Game()