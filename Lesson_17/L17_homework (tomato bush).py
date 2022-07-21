class Tomato:
    states = {0: "green", 1: "breakers", 2: "turning", 3: "pink", 4: "light red", 5: "red"}

    def __init__(self, index=0):
        self._index = index
        self._state = Tomato.states[self._index]

    def grow(self):
        self._index += 1 if self._index < 5 else 0
        self._state = Tomato.states[self._index]

    def is_ripe(self):
        return self._index == 5

    def get_state(self):
        return self._state


class TomatoBush:
    def __init__(self, fruits_num):
        self.tomatoes = [Tomato() for _ in range(fruits_num)]

    def grow_all(self):
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        return all(t.is_ripe() for t in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant=None):
        self.name = name
        self._plant = plant

    def work(self, plant=None):
        if plant:
            self._plant = plant
        print(f"{self.name} is working on a plant...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"All are ripe. {self.name} picked {len(self._plant.tomatoes)} tomatoes!")
            self._plant.give_away_all()
        else:
            print(f"It's too early: tomatoes are just {self._plant.tomatoes[0].get_state()}")

    @staticmethod
    def knowledge_base():
        info = [
            "TOMATO GROWING TIPS:",
            "Preheat soil",
            "Don't crowd tomatoes",
            "Provide lots of light",
            "Water and fertilize often",
            "Stake and prune plants",
            "Harvest your tomatoes"]

        for n, line in enumerate(info):
            print(line if not n else f"{n}.  {line};")
        print()


bush1 = TomatoBush(3)
gardener1 = Gardener("Nick")  # bush can be assigned initially by stating: Gardener("Nik", bush1)
Gardener.knowledge_base()
for _ in range(4):
    gardener1.work(bush1)    # plant parameter could be missed if specified initially: gardener1.work()
gardener1.harvest()          # try to harvest when it's too early
gardener1.work()
gardener1.harvest()          # this time tomatoes are ripe
