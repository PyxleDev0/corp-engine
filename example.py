from corpengine2 import *

Engine = InitEngine(960, 540, "Corporation")
Game = Engine.game  # TODO change the game to be capitalized

NewEntity("Player", Game.Workspace)

Engine.Mainloop()
