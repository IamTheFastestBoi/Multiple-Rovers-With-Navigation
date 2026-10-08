import time
import os
import random
class Smart_Rover_1:
    def __init__(self , name , map1 , current_position = (0, 0)):
        self.name = name
        self.current_position = current_position
        self.map1 = map1
        self.previous_positions = []
        self.successfull_routes = []

    def move(self):
        if  len(self.successfull_routes) > 0:
            selected_route = min(self.successfull_routes, key=len)
            self.previous_positions.append(self.current_position)
            self.current_position = selected_route[0]
            self.successfull_routes = [] 
        else:
            return False


    def memory(self):
        self.explored_positions = []
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.map1[current_position[0]][current_position[1]] == 2:
                self.successfull_routes.append(current_path)
                continue
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.map1) and 0 <= new_position[1] < len(self.map1[0]):
                    is_passable = (self.map1[new_position[0]][new_position[1]] == 0) or (self.map1[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.previous_positions and new_position not in current_path and new_position != self.current_position and new_position not in self.explored_positions:
                            new_path = current_path + [new_position]
                            current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
                            self.explored_positions.append(new_position)
    def backtrack(self):
        if len(self.previous_positions) > 0:
            self.current_position = self.previous_positions.pop()
            self.successfull_routes = []
        else:
            return False

class Smart_Rover_2:
    def __init__(self , name , map1 , current_position = (0, 0)):
        self.name = name
        self.current_position = current_position
        self.map1 = map1
        self.previous_positions = []
        self.successfull_routes = []

    def move(self):
        if  len(self.successfull_routes) > 0:
            selected_route = min(self.successfull_routes, key=len)
            self.previous_positions.append(self.current_position)
            self.current_position = selected_route[0]
            self.successfull_routes = [] 
        else:
            return False


    def memory(self):
        self.explored_positions = []
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.map1[current_position[0]][current_position[1]] == 2:
                self.successfull_routes.append(current_path)
                continue
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.map1) and 0 <= new_position[1] < len(self.map1[0]):
                    is_passable = (self.map1[new_position[0]][new_position[1]] == 0) or (self.map1[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.previous_positions and new_position not in current_path and new_position != self.current_position and new_position not in self.explored_positions:
                            new_path = current_path + [new_position]
                            current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
                            self.explored_positions.append(new_position)
    def backtrack(self):
        if len(self.previous_positions) > 0:
            self.current_position = self.previous_positions.pop()
            self.successfull_routes = []
        else:
            return False

class Smart_Rover_3:
    def __init__(self , name , map1 , current_position = (0, 0)):
        self.name = name
        self.current_position = current_position
        self.map1 = map1
        self.previous_positions = []
        self.successfull_routes = []

    def move(self):
        if  len(self.successfull_routes) > 0:
            selected_route = min(self.successfull_routes, key=len)
            self.previous_positions.append(self.current_position)
            self.current_position = selected_route[0]
            self.successfull_routes = [] 
        else:
            return False


    def memory(self):
        self.explored_positions = []
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.map1[current_position[0]][current_position[1]] == 2:
                self.successfull_routes.append(current_path)
                continue
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.map1) and 0 <= new_position[1] < len(self.map1[0]):
                    is_passable = (self.map1[new_position[0]][new_position[1]] == 0) or (self.map1[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.previous_positions and new_position not in current_path and new_position != self.current_position and new_position not in self.explored_positions:
                            new_path = current_path + [new_position]
                            current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
                            self.explored_positions.append(new_position)
    def backtrack(self):
        if len(self.previous_positions) > 0:
            self.current_position = self.previous_positions.pop()
            self.successfull_routes = []
        else:
            return False

class Smart_Rover_4:
    def __init__(self , name , map1 , current_position = ( 0 , 0)):
        self.name = name
        self.current_position = current_position
        self.map1 = map1
        self.previous_positions = []
        self.successfull_routes = []

    def move(self):
        if  len(self.successfull_routes) > 0:
            selected_route = min(self.successfull_routes, key=len)
            self.previous_positions.append(self.current_position)
            self.current_position = selected_route[0]
            self.successfull_routes = [] 
        else:
            return False


    def memory(self):
        self.explored_positions = []
        last_pos = self.previous_positions[-1] if len(self.previous_positions) > 0 else None
        current_spys = [{"position" : self.current_position , "step" : 0 , "previous_position" : last_pos , "path" : []}]
        while current_spys:
            current_spy = current_spys.pop(0)
            current_position = current_spy["position"]
            current_step = current_spy["step"]
            previous_position = current_spy["previous_position"]
            current_path = current_spy["path"]
            if self.map1[current_position[0]][current_position[1]] == 2:
                self.successfull_routes.append(current_path)
                continue
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if 0 <= new_position[0] < len(self.map1) and 0 <= new_position[1] < len(self.map1[0]):
                    is_passable = (self.map1[new_position[0]][new_position[1]] == 0) or (self.map1[new_position[0]][new_position[1]] == 2)
                    if is_passable:
                        if new_position not in self.previous_positions and new_position not in current_path and new_position != self.current_position and new_position not in self.explored_positions:
                            new_path = current_path + [new_position]
                            current_spys.append({"position": new_position, "step": current_step + 1, "previous_position": current_spy["position"], "path": new_path})
                            self.explored_positions.append(new_position)
    def backtrack(self):
        if len(self.previous_positions) > 0:
            self.current_position = self.previous_positions.pop()
            self.successfull_routes = []
        else:
            return False

import random

def generate_map(): # Made by AI

    new_map = [[1 for _ in range(50)] for _ in range(50)]
    

    stack = [(1, 1)]
    new_map[1][1] = 0
    
    while stack:
        cx, cy = stack[-1]

        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < 49 and 0 < ny < 49 and new_map[nx][ny] == 1:
                neighbors.append((nx, ny, cx + dx // 2, cy + dy // 2))
                
        if neighbors:
            nx, ny, wx, wy = random.choice(neighbors)
            new_map[wx][wy] = 0  
            new_map[nx][ny] = 0  
            stack.append((nx, ny))
        else:
            stack.pop()
            

    for _ in range(200):
        rx = random.randint(1, 48)
        ry = random.randint(1, 48)
        if new_map[rx][ry] == 1:
            path_count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= rx+dx < 50 and 0 <= ry+dy < 50 and new_map[rx+dx][ry+dy] == 0:
                    path_count += 1
            if path_count >= 2:
                new_map[rx][ry] = 0


    for i in range(23, 27):
        for j in range(23, 27):
            new_map[i][j] = 0
            
    new_map[24][24] = 2
    new_map[24][25] = 2
    new_map[25][24] = 2
    new_map[25][25] = 2
    

    spawn_points = [(1, 1), (1, 48), (48, 1), (48, 48)]
    for sx, sy in spawn_points:
        new_map[sx][sy] = 0

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= sx+dx < 50 and 0 <= sy+dy < 50:
                new_map[sx+dx][sy+dy] = 0

    return new_map




def simulation(map_current):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- OTONOM SÜRÜ SİMÜLASYONU ---")
    
    for satir in map_current:
        satir_gorseli = ""
        for hucre in satir:
            if hucre == 0:
                satir_gorseli += "⬜ "  
            elif hucre == 1:
                satir_gorseli += "⬛ "  
            elif hucre == 2:
                satir_gorseli += "🎯 "  
            elif hucre == 3:
                satir_gorseli += "🤖 "  
        print(satir_gorseli)
    
    print("-------------------------------")



map_current = generate_map()

my_rover_1 = Smart_Rover_1(name= "Smart Rover_1", map1=map_current, current_position=(1, 1))
my_rover_2 = Smart_Rover_2(name= "Smart Rover_2", map1=map_current, current_position=( 1,48 ))
my_rover_3 = Smart_Rover_3(name= "Smart Rover_3", map1=map_current, current_position=( 48, 1 ))
my_rover_4 = Smart_Rover_4(name= "Smart Rover_4", map1=map_current, current_position=( 48, 48 ))

rovers = [my_rover_1, my_rover_2, my_rover_3, my_rover_4]
targets = [(24, 24), (24, 25), (25, 24), (25, 25)]

while True:
    active_rovers = []
    for rover in rovers:
        if rover.current_position in targets:
            map_current[rover.current_position[0]][rover.current_position[1]] = 2
            continue
        map_current[rover.current_position[0]][rover.current_position[1]] = 0
        rover.memory()
        if rover.move() == False:
            rover.backtrack()
        map_current[rover.current_position[0]][rover.current_position[1]] = 3
        active_rovers.append(rover)
    rovers = active_rovers
    simulation(map_current)
    time.sleep(0.5)
    if len(rovers) == 0:
        print("ALL ROVERS SUCCESSFULLY REACHED THE TARGET!")
        break











