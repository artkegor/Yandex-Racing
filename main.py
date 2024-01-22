from data.gameFiles.game import Game

g = Game()

while g.running:
    g.current_menu.display_menu()
    while g.playing:
        # Начало игры
        g.game_loop()
