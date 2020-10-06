import unittest
import robot
from io import StringIO
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    #@patch("sys.stdin", StringIO("forward 10\noff\n"))
    def test_update_c_history(self):
        '''
        robot.update_c_history("forward 10")
        self.assertEqual(robot.command_list[0],'forward 10')
        robot.update_c_history("back 22")
        self.assertEqual(robot.command_list[1],'back 22')
        '''
        pass
        
    def test_retrieve_commands(self):
        '''
        robot.update_c_history("forward 10")
        self.assertEqual(['forward 10'], robot.retrieve_commands())
        '''
        pass

    def test_do_replay(self):
        pass

    def test_do_replay_reversed(self):
        pass

    def test_do_replay_reversed_silent(self):
        pass

    def test_replay_silent(self):
        pass

    def test_get_robot_name(self):
        pass

    def test_get_command(self):
        pass

    def test_split_command_input(self):
        pass

    def test_is_int(self):
        pass

    def test_valid_range(self):
        pass

    def test_number_of_replays(self):
        pass

    def test_valid_command(self):
        pass

    def test_output(self):
        pass

    def test_do_help(self):
        pass

    def test_show_position(self):
        pass

    def test_is_position_allowed(self):
        pass

    def test_update_position(self):
        pass

    def test_do_forward(self):
        pass

    def test_do_back(self):
        pass

    def test_do_right_turn(self):
        pass

    def test_do_left_turn(self):
        pass

    def test_do_sprint(self):
        pass

    def test_handle_command(self):
        pass


