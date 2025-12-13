


class AocUtil:

    def __init__(self, splitter = '\n'):
        self.splitter = splitter

    def load_aoc_25(self, task):
        return self.load_aoc_file(25, task)

    def load_aoc_file(self, year, task):
        with open('../../resources/adv' + str(year) + '/' + str(task).zfill(2) + '_inp.txt') as list_file:
            return [char for char in list_file.read().split(self.splitter) if char != ""]