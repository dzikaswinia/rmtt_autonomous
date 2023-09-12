import unittest
import state
import command

"""
class TestPositionSetting(unittest.TestCase):
    def runTest(self):
        pos = [100,100,0,0]
        rectangle = state_tracker.State(pos)
        self.assertEqual(rectangle.pos, pos, "incorrect position")



class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)
"""




class TestUpdatingCoordinates(unittest.TestCase):
    def runTest(self):
        # setup
        pos = [100,100,0,270]
        state = state_tracker.Position(pos)
        cmd = command.Command("cw", 180)
        state.update(cmd)
        updated_pos = [100, 100, 0, 90]

        # exec
        self.assertEqual(state.pos, updated_pos, "incorrect position update with cmd \"up\"")

    def runTest2(self):
        # setup
        pos = [100,100,0,90]
        state = state_tracker.Position(pos)
        cmd = command.Command("cw", 180)
        state.update(cmd)
        updated_pos = [100, 100, 0, 270]

        # exec
        self.assertEqual(state.pos, updated_pos, "incorrect position update with cmd \"up\"")







if __name__ == '__main__':
    unittest.main()