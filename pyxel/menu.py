import pyxel as px
from game import Game

class Menu():
    '''
    Telas:
        [None] Menu
        [0] Configurações
        [1] Jogar
    '''
    def __init__(self):
        px.init(1000, 600, 'Pong', quit_key=px.KEY_ESCAPE)
        px.load('./game.pyxres')
        px.mouse(True)
        self.game = Game()
        self.screen = None
        self.BUTTONS = {
            'width': 210,
            'height': 70,
            'x': px.width/2 - 210/2, # width
            '1 player': px.height/3 - 70/2, # height
            '2 players': px.height/3 + 70/2 + 20, # height
            'configurations': px.height/3 + 1.5 * 70 + 40, # height
            'unselect': 8,
            'select': 9
        }
        px.run(self.update_menu, self.draw_menu)
        
    def update_menu(self):
        if px.btnp(px.KEY_ESCAPE):
            px.quit

        if px.btnp(px.KEY_0):
            self.game.players = 1
            px.run(self.game.update_game, self.game.draw_game)
        if px.btnp(px.KEY_1):
            self.game.players = 2
            px.run(self.game.update_game, self.game.draw_game)
    
    def draw_menu(self):
        px.cls(14)

        self.update_buttons()
        

    def update_buttons(self):
        if self.BUTTONS['x'] <= px.mouse_x <= self.BUTTONS['x'] + self.BUTTONS['width']:
            if self.BUTTONS['1 player'] <= px.mouse_y <= self.BUTTONS['1 player'] + self.BUTTONS['height']:
                px.rect(self.BUTTONS['x'], self.BUTTONS['1 player'], self.BUTTONS['width'], self.BUTTONS['height'], self.BUTTONS['select'])
            else:
                px.rect(self.BUTTONS['x'], self.BUTTONS['1 player'], self.BUTTONS['width'], self.BUTTONS['height'], self.BUTTONS['unselect'])
        else:
                px.rect(self.BUTTONS['x'], self.BUTTONS['1 player'], self.BUTTONS['width'], self.BUTTONS['height'], self.BUTTONS['unselect'])


    
