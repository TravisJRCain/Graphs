from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}
reversed_traversal_path = []
directions = {"n": "s", "e": "w", "s": "n", "w": "e"}

# add exit paths to the player in their current room
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        # last room in traversal path array
        previous_room = reversed_traversal_path[-1]
        # remove previous room from consideration
        visited[player.current_room.id].remove(previous_room)

    if len(visited[player.current_room.id]) == 0:
        previous_room = reversed_traversal_path[-1]
        # remove and return the last value from the list
        reversed_traversal_path.pop()
        # add previous room
        traversal_path.append(previous_room)
        # denote that player traveled to previous room
        player.travel(previous_room)
    else:
        visit = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        traversal_path.append(visit)
        reversed_traversal_path.append(directions[visit])
        player.travel(visit)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
