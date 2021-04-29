import logging
import unittest
from . import memory
from . import exceptions
ha

class IntcodeComputer:
    exceptions = exceptions
    normal_exceptions = (exceptions.Finished, exceptions.WaitingForInput, exceptions.WaitingForOutput)

    def __init__(self, initial_memory=None):
        self.memory = memory.Memory(initial_memory or [])
        self.log = logging.getLogger(self.__class__.__name__)
        self.opcode_map = {
            1: self.addition,
            2: self.multiplication,
            3: self.raise_input,
            4: self.raise_output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.relative_base,
            99: self.finish
        }
        self.input_ready = False
        self.output_ready = False

    def addition(self):
        self.memory.set(self.memory.get() + self.memory.get())

    def multiplication(self):
        self.memory.set(self.memory.get() * self.memory.get())

    def raise_input(self):
        self.input_ready = True
        raise exceptions.WaitingForInput

    def input(self, v):
        if self.input_ready:
            self.input_ready = False
            self.memory.set(v)
        else:
            raise exceptions.NotExpectingInput

    def raise_output(self):
        self.output_ready = True
        raise exceptions.WaitingForOutput

    def output(self):
        if self.output_ready:
            self.output_ready = False
            return self.memory.get()
        else:
            raise exceptions.NotExpectingOutput

    def jump_if_true(self):
        if self.memory.get():
            self.memory.i = self.memory.get()
        else:
            self.memory.get()

    def jump_if_false(self):
        if self.memory.get():
            self.memory.get()
        else:
            self.memory.i = self.memory.get()

    def less_than(self):
        self.memory.set(int(self.memory.get() < self.memory.get()))

    def equals(self):
        self.memory.set(int(self.memory.get() == self.memory.get()))

    def relative_base(self):
        self.memory.relative_base += self.memory.get()

    def finish(self):
        raise exceptions.Finished

    def process(self):
        while opcode := self.memory.get_opcode():
            self.log.debug(f"{opcode}, {self.memory}")
            operation = self.opcode_map.get(opcode)
            if operation:
                operation()
            else:
                raise exceptions.UnknownOpCode(opcode)

    def run(self):
        try:
            self.process()
        except IntcodeComputer.normal_exceptions:
            pass
