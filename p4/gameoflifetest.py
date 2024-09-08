import game_of_life
nr=20
nc= 20
#nr= 5
#nc= 8
add_rule= True
world= game_of_life.create_world(nr, nc, "random")
print(world)
print(game_of_life.one_generation_later(world,False))
#print(game_of_life.simulate(6, nr, nc, "random", False, .9))
print(game_of_life.simulate(8, nr, nc, 'seeds_glider.txt', False, .9))

#print()

