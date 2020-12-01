from . import exceptions
import logging


class Memory:
    def __init__(self, memory=None, i=0):
        self.memory = dict()
        self.i = i
        self.pmi = None
        self.relative_base = 0
        if memory:
            self.load(memory)

    def __repr__(self):
        return f"{self.memory}"

    def __iter__(self):
        self.mi = 0
        self.pi = 0

    def __next__(self):
        i = self.i
        self.i += 1
        try:
            return self.memory[i]
        except KeyError:
            raise exceptions.RanOut

    def reset(self):
        self.i = 0

    def load(self, new_memory):
        self.reset()
        self.memory = dict()
        for i, v in enumerate(new_memory):
            self.memory[i] = v

    def get_opcode(self):
        raw = next(self)
        padded = str(raw).rjust(5, '0')
        opcode = int(padded[-2:])
        self.pmi = iter(list(map(int, list(padded[:3][::-1]))))
        return opcode

    def set(self, value):
        pm = next(self.pmi)
        if pm == 0:
            address = next(self)
        elif pm == 2:
            address = self.relative_base + next(self)
        else:
            raise exceptions.UnknownParameterMode(pm)

        self.memory[address] = value

    def get(self):
        pm = next(self.pmi)
        if pm == 0:
            address = next(self)
        elif pm == 1:
            return next(self)
        elif pm == 2:
            address = self.relative_base + next(self)
            return self.memory[address]
        else:
            raise exceptions.UnknownParameterMode(pm)

        if address not in self.memory:
            self.memory[address] = 0
        return self.memory[address]
