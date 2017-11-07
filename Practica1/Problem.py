import random
import State
import StateOperations

class Problem:




    def __init__(self, increase, depth_max, path, state):
        self.increase = increase
        self.depth_max = depth_max
        self.path = path
        self.state = state
        self.spaceState = StateOperations.StateOperations(self.state)


    def get_Increase(self):
        return self.increase

    def set_Increase(self, increase):
        self.increase = increase

    def get_DepthMax(self):
        return self.depth_max

    def set_DepthMax(self, depth_max):
        self.depth_max = depth_max

    def choose_option(self):
        while True:
            choice = input('From where do you want to load the data?\n1.- From file.\n2.- Random generated.\n')
            if choice == '1':
                self.read_file(self.state)
                break
            elif choice == '2':
                self.generate_terrain(self.state)
                break
            else:
                print("'"+choice+"' is not a valid option. Please, try again.")


    def generate_terrain(self, state):
        te = input('¿ De cuanto quieres el terreno?(ZxZ)')
        tr = input('¿Donde quieres que se coloque el tractor?(ZxZ)')
        k = input('¿Que valor quieres que sea el ideal para cada celda?')
        maximum = input('Cual quieres que sea el valor maximo de cada celda?')

        # Create the terrain
        state.cols = int(te[2])
        state.rows = int(te[0])
        state.x_tractor = int(tr[0])
        state.y_tractor = int(tr[2])
        state.k = int(k)
        state.max = int(maximum)

        # Fill the terrain with values
        state.terrain_representation = [[[] for i in range(int(state.cols))] for j in range(int(state.rows))]
        for i in range(int(te[2])):
            for j in range(int(te[0])):
                ran = str(random.randint(0, int(maximum)))
                state.terrain_representation[i][j] = ran

    def read_file(self, state):
        try:
            with open(self.path) as f:
                file = f.read().splitlines()
                # Read configuration controls
                config = file[0].split(" ")
                tractor_x, tractor_y, k, maximum, col, row = config[0], config[1], config[2], config[3], config[4], \
                                                         config[5]
                # Create the terrain
                state.cols = int(col)
                state.rows = int(row)
                state.x_tractor = int(tractor_x)
                state.y_tractor = int(tractor_y)
                state.k = int(k)
                state.max = int(maximum)

                # Fill the terrain with values
                state.terrain_representation = [[[] for i in range(int(state.cols))] for i in range(int(state.rows))]
                for i in range(int(row)):
                    row_values = file[i + 1].split(" ")
                    print(row_values)
                    state.terrain_representation[i] = row_values
                state.print_terrain()

        except Exception as ex:
            print(ex.__str__())


    def write_file(self, successors):
        try:
            with open("./successors.txt", "w") as f:
                f.write("Length of successors: {}\n".format(len(successors)))
                for successor in successors:
                    f.write("{}\n".format(str(successor)))
        except Exception as ex:
            print(ex.__str__())

