


class Route():
    n_instances = 0

    def __init__(self):
        Route.n_instances += 1
        self.id = Route.n_instances -1
        