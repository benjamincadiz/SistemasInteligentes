class Node:
    def __init__(self, state, cost, action, value, parent, depth):
        self.__state = state
        self.__cost = cost
        self.__action = action
        self.__value = value
        self.__parent = parent
        self.__depth = depth

    def get_state(self):
        return self.__state

    def get_cost(self):
        return self.__cost

    def get_action(self):
        return self.__action

    def get_value(self):
        return self.__value

    def get_parent(self):
        return self.__parent

    def get_depth(self):
        return self.__depth

    def create_node(self, sucessor, actual_node, strategy, max_depth):
        depth = actual_node.get_depth() + 1
        cost=actual_node.get_cost+sucessor[2] #sumamos el coste que produce llegar al sucesor
        if (strategy == 'DFS'):
            value = depth
        elif(strategy=='BFS') or (strategy=='IT'):
            value=max_depth-depth
        elif(strategy=='UC'):
            value= cost

        new_node=Node(sucessor[1], cost, sucessor[0], value, actual_node, depth)
        return new_node

