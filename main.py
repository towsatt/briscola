from env import *

def p1_vs_cpu():
    env = Virtual_env()
    env.start()
    while len(env.p1.hand):
        env.game_turn()

def p1_vs_p2():
    pass

env_type = 1

if env_type:
    p1_vs_cpu()
else:
    p1_vs_p2()