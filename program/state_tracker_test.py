import unittest
import state_tracker
import command


class TestPositionSetting(unittest.TestCase):
    def runTest(self):
        pos = [100,100,0,0]
        rectangle = state_tracker.State(pos)
        self.assertEqual(rectangle.pos, pos, "incorrect position")


class TestUpdatingCoordinates(unittest.TestCase):
    def runTest(self):
        # setup
        pos = [100,100,0,0]
        state = state_tracker.State(pos)
        cmd = command.Command("up", 20)
        state.update(cmd)
        updated_pos = [100, 100, 20, 0]

        # exec
        self.assertEqual(state.pos, updated_pos, "incorrect position update with cmd \"up\"")



unittest.main()