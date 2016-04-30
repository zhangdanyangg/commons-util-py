from unittest import TestCase
import pickle
from util.commons_util.fundamentals.pickle.copyreg_demo import *


__author__ = 'Daniel'


class TestSerialization(TestCase):
    def test_copyreg(self):
        state = State()
        state.points += 1000
        serialized = pickle.dumps(state)
        state_after = pickle.loads(serialized)
        print(state_after.__dict__)