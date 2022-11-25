from classes import Game

if __name__ == "__main__":
    game = Game(["Astha", "Varun", "Nancy", "Geetha"], 100, 1, {6:1, 15:9, 23:11, 35:19, 56:46, 73:23, 86:13, 99:3}, {2:12, 10:30, 20:25, 36:59, 21:28, 75:85, 88:91})
    game.play()